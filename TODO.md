### Todo

- [ ] Add a first AI agent to handle the user input, check everything is correct and asked before sending to the big crew
- [ ] Clean up code
- [ ] Write proper documentation
- [ ] Output intermediate files within the appropriate logs folder
- [ ] Fix [EventBus Error] Handler 'on_task_failed' failed for event 'TaskFailedEvent': 'TaskFailedEvent' object has no attribute 'error_message'
- [ ] Fix [EventBus Error] Handler 'on_crew_failed' failed for event 'CrewKickoffFailedEvent': 'CrewKickoffFailedEvent' object has no attribute 'error_message'
- [ ] Add python debugger
- [ ] Instead of asking LLMs to copy/paste URLs between tasks, extract manually and add them to the final output
- [ ] Explain state of the project and why it won't go further + lessons + limitations
- [ ] Clean up readme and such for pro output

### In Progress

- [ ] Add intermediate outputs from the other crew agents in gradio/listeners

### Done ✓

- [x] Reworked Teacher AI to output clean, professional and structured output