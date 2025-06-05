from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

import streamlit as st

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
        Conduct a thorough research about {topic}.
        Make sure you find any interesting and relevant information given
        the current year is 2025.
        """,
      expected_output="""
        A list with 10 bullet points of the most relevant information about {topic}
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

## Streamlit

st.title("PharmaAI Chat")

# Set a default model
if "ai_model" not in st.session_state:
    st.session_state["ai_model"] = "deepseek-r1-0528"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        crew_output = research_crew.kickoff(inputs={'topic': prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write(crew_output.raw)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})