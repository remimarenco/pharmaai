import asyncio
from crewai.utilities.events.base_event_listener import BaseEventListener
from crewai.utilities.events import (
    CrewKickoffStartedEvent,
    CrewKickoffCompletedEvent,
    CrewKickoffFailedEvent,
    AgentExecutionStartedEvent,
    AgentExecutionCompletedEvent,
    AgentExecutionErrorEvent,
    TaskStartedEvent,
    TaskCompletedEvent,
    TaskFailedEvent,
    ToolUsageStartedEvent,
    ToolUsageFinishedEvent,
    ToolUsageErrorEvent,
    LLMStreamChunkEvent, # Important for detailed streaming
)
# Gradio ChatMessage is not strictly needed here if we pass dicts
# from gradio import ChatMessage 

class GradioCrewListener(BaseEventListener):
    def __init__(self, output_queue: asyncio.Queue, loop: asyncio.AbstractEventLoop):
        super().__init__()
        self.output_queue = output_queue
        self.main_loop = loop
        self.thinking_message_id_counter = 0

    def _put_message(self, content, title=None, status="pending", is_final=False):
        """Helper to create and queue message data (as dicts)."""
        if is_final:  # This is the actual final output of the crew
            msg_data = {
                "content": content,
                "metadata": {"is_crew_final_output": True}
            }
        else:  # This is an intermediate step or a status update
            self.thinking_message_id_counter += 1
            msg_data = {
                "content": content,
                "metadata": {
                    "id": f"crew_event_{self.thinking_message_id_counter}",
                    "status": status
                }
            }
            if title:
                msg_data["metadata"]["title"] = title
        
        asyncio.run_coroutine_threadsafe(self.output_queue.put(msg_data), self.main_loop)

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(CrewKickoffStartedEvent)
        def on_crew_started(source, event: CrewKickoffStartedEvent):
            self._put_message(f"Crew '{event.crew_name}' has started execution!", title="Crew Status")

        @crewai_event_bus.on(AgentExecutionStartedEvent)
        def on_agent_started(source, event: AgentExecutionStartedEvent):
            agent_name = getattr(event.agent, 'role', 'Unknown Agent')
            task_description = getattr(event.task, 'description', 'Unknown Task')
            self._put_message(f"Agent '{agent_name}' starting task: {task_description}", title="Agent Action")

        @crewai_event_bus.on(ToolUsageStartedEvent)
        def on_tool_started(source, event: ToolUsageStartedEvent):
            tool_input_str = str(event.tool_input)
            max_len_input = 100
            if len(tool_input_str) > max_len_input:
                tool_input_str = tool_input_str[:max_len_input] + "..."
            self._put_message(f"Tool '{event.tool_name}' started with input: {tool_input_str}", title="Tool Usage")
        
        @crewai_event_bus.on(ToolUsageFinishedEvent)
        def on_tool_finished(source, event: ToolUsageFinishedEvent):
            output_str = str(event.output)
            max_len_output = 150
            if len(output_str) > max_len_output:
                output_str = output_str[:max_len_output] + "..."
            self._put_message(f"Tool '{event.tool_name}' finished. Output: {output_str}", title="Tool Usage", status="done")

        @crewai_event_bus.on(TaskCompletedEvent)
        def on_task_completed(source, event: TaskCompletedEvent):
            task_desc = getattr(event.task, 'description', 'Unknown Task')
            # Attempt to get agent information from the task associated with the event
            agent_obj = getattr(event.task, 'agent', None)
            agent_role = getattr(agent_obj, 'role', 'Unknown Agent')
            self._put_message(f"Task '{task_desc}' completed by agent '{agent_role}'.", title="Task Status", status="done")

        @crewai_event_bus.on(AgentExecutionCompletedEvent)
        def on_agent_execution_completed(source, event: AgentExecutionCompletedEvent):
            agent_name = getattr(event.agent, 'role', 'Unknown Agent')
            self._put_message(f"Agent '{agent_name}' completed its execution.", title="Agent Status", status="done")

        @crewai_event_bus.on(CrewKickoffCompletedEvent)
        def on_crew_completed(source, event: CrewKickoffCompletedEvent):
            self._put_message(f"Crew '{event.crew_name}' has completed execution!", title="Crew Status", status="done")
            final_output_content = getattr(event.output, 'raw', str(event.output))
            # This is the actual final payload, sent with is_final=True
            self._put_message(final_output_content, is_final=True)
            asyncio.run_coroutine_threadsafe(self.output_queue.put(None), self.main_loop) # Signal end

        @crewai_event_bus.on(CrewKickoffFailedEvent)
        def on_crew_failed(source, event: CrewKickoffFailedEvent):
            # This failure message is the final payload in case of error, sent with is_final=True
            self._put_message(f"Crew '{event.crew_name}' failed: {event.error_message}", is_final=True)
            asyncio.run_coroutine_threadsafe(self.output_queue.put(None), self.main_loop) # Signal end
        
        @crewai_event_bus.on(AgentExecutionErrorEvent)
        def on_agent_error(source, event: AgentExecutionErrorEvent):
            agent_name = getattr(event.agent, 'role', 'Unknown Agent')
            self._put_message(f"Error during execution of agent '{agent_name}': {str(event.error)}", title="Agent Error", status="error")

        @crewai_event_bus.on(TaskFailedEvent)
        def on_task_failed(source, event: TaskFailedEvent):
            task_desc = getattr(event.task, 'description', 'Unknown Task')
            self._put_message(f"Task '{task_desc}' failed: {str(event.error_message)}", title="Task Error", status="error")

        @crewai_event_bus.on(ToolUsageErrorEvent)
        def on_tool_error(source, event: ToolUsageErrorEvent):
            self._put_message(f"Error using tool '{event.tool_name}': {str(event.error)}", title="Tool Error", status="error")
