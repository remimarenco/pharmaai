import gradio as gr
from gradio import ChatMessage
import dotenv
import os
from openai import OpenAI
from crewai import Agent, Crew, Process, Task, LLM
from crewai.agents.agent_builder.base_agent import BaseAgent
from datetime import datetime
import time
import asyncio
from crewai.utilities.events import crewai_event_bus
from pharmaai.gradio_listener import GradioCrewListener
from pharmaai.crew import Pharmaai
from fastapi import FastAPI

app = FastAPI()

sleep_time = 0.5

dotenv.load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key)

## Crew
research_analyst = Agent(
      role="Research Analyst",
      goal="Find and summarize information about specific topics",
      backstory="You are an experienced researcher with attention to detail",
      llm=LLM(
        model="openrouter/deepseek/deepseek-chat-v3-0324:free"
      ),
      verbose=True  # Enable logging for debugging
    )

research_task = Task(
      description="""
        Conduct a thorough research about the pharmacological question asked by the user : {question_pharmacienne}.
        Make sure you find any interesting and relevant information given
        the current year is {current_year}.
        """,
      expected_output="""
        A list with 10 bullet points of the most relevant information about : {question_pharmacienne}. Answer in French.
      """,
      agent=research_analyst,
      markdown=True
    )


research_crew = Crew(
      agents=[research_analyst],
      tasks=[research_task],
      process=Process.sequential,
      verbose=True,
    )

def predict(message, history):
    history.append({"role": "user", "content": message})
    stream = client.chat.completions.create(
        messages=history,
        model="deepseek/deepseek-chat-v3-0324:free",
        stream=True
    )
    chunks = []
    for chunk in stream:
        chunks.append(chunk.choices[0].delta.content or "")
        yield "".join(chunks)

async def call_crew(message: str, history: list):
    current_crew_instance = Pharmaai().crew()
    inputs = {
        'question_pharmacienne': message,
        'current_year': str(datetime.now().year)
    }

    event_queue = asyncio.Queue()
    loop = asyncio.get_running_loop()
    listener_for_this_run = GradioCrewListener(event_queue, loop)

    # Accumulators for content
    accumulated_intermediate_content = ""
    final_crew_output_content = "No final output received."
    behind_the_scenes_message = None

    with crewai_event_bus.scoped_handlers():
        listener_for_this_run.setup_listeners(crewai_event_bus)
        crew_task = asyncio.create_task(current_crew_instance.kickoff_async(inputs=inputs))

        try:
            while True:
                try:
                    event_data = await asyncio.wait_for(event_queue.get(), timeout=0.1)
                    if event_data is None:  # End of queue signal from listener
                        break

                    event_content = event_data.get("content", "")
                    event_metadata = event_data.get("metadata", {})

                    if event_metadata.get("is_crew_final_output"):
                        final_crew_output_content = event_content
                        # The final output is stored; we will yield it as part of the final list.
                    else:
                        # This is an intermediate, 'behind the scenes' update
                        event_title = event_metadata.get('title', 'Update')
                        formatted_event_content = f"**{event_title}:**\n{event_content}"
                        
                        if accumulated_intermediate_content:
                            accumulated_intermediate_content += "\n\n---\n\n"  # Separator
                        accumulated_intermediate_content += formatted_event_content

                        # Create or update the single 'Behind the Scenes' message
                        behind_the_scenes_message = gr.ChatMessage(
                            role="assistant",
                            content=accumulated_intermediate_content,
                            metadata={"title": "Behind the Scenes", "status": "pending"}
                        )
                        yield behind_the_scenes_message
                    
                    event_queue.task_done()

                except asyncio.TimeoutError:
                    if crew_task.done():
                        break  # Crew finished and queue is empty
                    # else: continue, queue is empty, but crew still running
                except Exception as e:
                    error_message_detail = f"Error processing event: {str(e)}\n{traceback.format_exc()}"
                    print(error_message_detail)
                    # Append error to intermediate content
                    error_display_content = f"**Error during processing:**\n{error_message_detail}"
                    if accumulated_intermediate_content:
                        accumulated_intermediate_content += "\n\n---\n\n" + error_display_content
                    else:
                        accumulated_intermediate_content = error_display_content
                    
                    # Update and yield the 'Behind the Scenes' message with the error
                    behind_the_scenes_message = gr.ChatMessage(
                        role="assistant",
                        content=accumulated_intermediate_content,
                        metadata={"title": "Behind the Scenes - Error", "status": "error"}
                    )
                    yield behind_the_scenes_message
                    # Consider if crew_task should be cancelled or if we should break
                    # For now, we log and continue, assuming listener might send 'None' or final error.
                    event_queue.task_done()
        finally:
            # Ensure crew task is awaited or cancelled to prevent pending task errors on shutdown
            if not crew_task.done():
                crew_task.cancel()
            try:
                await crew_task
            except asyncio.CancelledError:
                print("Crew task was cancelled.")
            except Exception as e:
                print(f"Exception from crew task: {e}")

    # --- Construct and yield the final list of two messages ---

    # 1. The 'Behind the Scenes' message (final state)
    # If an error occurred and was the last thing, status might be 'error'
    # Otherwise, if final_crew_output_content was set, it means crew completed.
    final_bts_status = "done"
    if behind_the_scenes_message and behind_the_scenes_message.metadata.get("status") == "error":
        final_bts_status = "error"
    elif not accumulated_intermediate_content: # If nothing happened behind the scenes
        accumulated_intermediate_content = "No intermediate steps were recorded."
        
    behind_the_scenes_final_msg = gr.ChatMessage(
        role="assistant",
        content=accumulated_intermediate_content,
        metadata={"title": "Behind the Scenes", "status": final_bts_status}
    )

    # 2. The 'Final Output' message
    final_output_msg = gr.ChatMessage(
        role="assistant",
        content=final_crew_output_content,
        metadata={} # No metadata as per requirement
    )

    yield [behind_the_scenes_final_msg, final_output_msg]

def simulate_thinking_chat(message, history):
    start_time = time.time()
    response = ChatMessage(
        content="",
        metadata={"title": "_Thinking_ step-by-step", "id": 0, "status": "pending"}
    )
    yield response

    thoughts = [
        "First, I need to understand the core aspects of the query...",
        "Now, considering the broader context and implications...",
        "Analyzing potential approaches to formulate a comprehensive answer...",
        "Finally, structuring the response for clarity and completeness..."
    ]

    accumulated_thoughts = ""
    for thought in thoughts:
        time.sleep(sleep_time)
        accumulated_thoughts += f"- {thought}\n\n"
        response.content = accumulated_thoughts.strip()
        yield response

    response.metadata["status"] = "done"
    response.metadata["duration"] = time.time() - start_time
    yield response

    response = [
        response,
        ChatMessage(
            content="Based on my thoughts and analysis above, my response is: This dummy repro shows how thoughts of a thinking LLM can be progressively shown before providing its final answer."
        )
    ]
    yield response

example_code = """
Here's an example Python lambda function:

lambda x: x + {}

Is this correct?
"""
def chat_value(message, history):
    if message == "Yes, that's correct.":
        return "Great!"
    else:
        return gr.ChatMessage(
            content=example_code.format(random.randint(1, 100)),
            options=[
                {"value": "Yes, that's correct.", "label": "Yes"},
                {"value": "No"}
            ]
        )

demo = gr.ChatInterface(call_crew, type="messages", save_history=True)

#demo.launch()


app = gr.mount_gradio_app(app, demo, path="/pharmaai")