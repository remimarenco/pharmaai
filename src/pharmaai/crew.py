import os
from typing import List, Any
import json
import dotenv
from datetime import datetime
from pathlib import Path

# Must precede any llm module imports
from langtrace_python_sdk import langtrace
dotenv.load_dotenv()
langtrace.init(os.getenv("LANGTRACE_API_KEY"))
from langchain_community.chat_models import ChatLiteLLM

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.agents.parser import AgentAction, AgentFinish

#from crewai_tools import EXASearchTool
from src.pharmaai.tools.pharmacie_exa_tool import EXASearchTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

from crewai.project import after_kickoff

@CrewBase
class Pharmaai():
    """Pharmaai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        from logging import getLogger, FileHandler, Formatter, INFO
        self.log_time = datetime.now().strftime("%Y-%m-%dT%H_%M")
        self.log_dir = Path("logs") / self.log_time
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.logger = getLogger(f"pharmaai_{self.log_time}")
        self.logger.setLevel(INFO)
        log_file = self.log_dir / "pharmaai.log"
        if not self.logger.handlers:
            file_handler = FileHandler(log_file, encoding='utf-8')
            file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s %(message)s'))
            self.logger.addHandler(file_handler)
        self.logger.info(f"Logger initialisé dans {log_file}")

    # --- AGENTS ---
    @agent
    def pharmacien_chercheur(self) -> Agent:
        exa_api_key = os.getenv("EXA_API_KEY")

        return Agent(
            config=self.agents_config['pharmacien_chercheur'],
            tools=[EXASearchTool(api_key=exa_api_key, content=True)],
            llm=ChatLiteLLM(model="openrouter/google/gemini-2.0-flash-001")
        )

    @agent
    def pharmacien_expert_clinique(self) -> Agent:
        return Agent(
            config=self.agents_config['pharmacien_expert_clinique'],
            llm=ChatLiteLLM(model="openrouter/google/gemini-2.0-flash-001")
        )

    @agent
    def pharmacien_pedagogue(self) -> Agent:
        return Agent(
            config=self.agents_config['pharmacien_pedagogue'],
            llm=ChatLiteLLM(model="openrouter/google/gemini-2.0-flash-001")
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    # --- TACHES ---
    @task
    def tache_recherche_information(self) -> Task:
        return Task(
            config=self.tasks_config['tache_recherche_information'],
        )

    @task
    def tache_analyse_clinique_et_synthese(self) -> Task:
        return Task(
            config=self.tasks_config['tache_analyse_clinique_et_synthese'],
        )

    @task
    def tache_formulation_pedagogique_reponse(self) -> Task:
        return Task(
            config=self.tasks_config['tache_formulation_pedagogique_reponse'],
        )

    def step_callback(self, agent_step: AgentAction | AgentFinish):
        log_path = self.log_dir / "steps.md"

        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"---\n\n")

            # Handle agent finishing a task
            if isinstance(agent_step, AgentFinish):
                f.write(f"## Agent Finish\n\n")
                f.write(f"**Thought:**\n```\n{agent_step.thought.strip() if agent_step.thought else ''}\n```\n\n")
                f.write(f"**Output:**\n```\n{agent_step.output.strip() if agent_step.output else ''}\n```\n\n")
                f.write(f"**Text:**\n```\n{agent_step.text.strip() if agent_step.text else ''}\n```\n\n")
                return

            # Handle agent taking an action
            if isinstance(agent_step, AgentAction):
                f.write(f"## Agent Action\n\n")
                f.write(f"**Thought:**\n```\n{agent_step.thought.strip() if agent_step.thought else ''}\n```\n\n")
                f.write(f"**Action:** `{agent_step.tool}`\n\n")
                tool_input = agent_step.tool_input
                if isinstance(tool_input, dict):
                    tool_input = json.dumps(tool_input, indent=2, ensure_ascii=False)
                f.write(f"**Action Input:**\n```\n{tool_input}\n```\n\n")
                return

            # Fallback for any other type (should ideally not be reached if typing is correct)
            f.write(f"## Unknown Step\n\n")

    @after_kickoff
    def log_crew_output(self, crew_output, **kwargs):
        import traceback
        def write_log_file(path, content, as_json=False):
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    if as_json:
                        json.dump(content, f, ensure_ascii=False, indent=2)
                    else:
                        f.write(str(content))
                self.logger.info(f"Fichier écrit : {path}")
            except Exception as e:
                self.logger.error(f"Échec d'écriture du fichier {path}: {e}")

        log_dir = self.log_dir
        log_items = [
            ("raw.txt", getattr(crew_output, 'raw', str(crew_output)), False, None),
            ("json_output.json", None, True, "No JSON output found in the final task."),
            ("pydantic.txt", getattr(crew_output, 'pydantic', None), False, None),
            ("tasks_output.txt", getattr(crew_output, 'tasks_output', None), False, None),
            ("token_usage.txt", getattr(crew_output, 'token_usage', None), False, None),
        ]

        # Write raw.txt
        write_log_file(log_dir / log_items[0][0], log_items[0][1])

        # Write json_output.json (always write a file)
        json_path = log_dir / log_items[1][0]
        try:
            json_dict = crew_output.json
            write_log_file(json_path, json_dict, as_json=True)
        except Exception as e:
            error_info = {
                "error": log_items[1][3],
                "exception": str(e),
                "traceback": traceback.format_exc()
            }
            write_log_file(json_path, error_info, as_json=True)

        # Write the rest (pydantic, tasks_output, token_usage)
        for filename, value, as_json, _ in log_items[2:]:
            if value is not None:
                write_log_file(log_dir / filename, value, as_json=as_json)

    @crew
    def crew(self) -> Crew:
        """Creates the Pharmaai crew"""
        # Utilise le log_dir et log_time déjà initialisés dans __init__
        output_log_file = self.log_dir / "Pharmaai_crew.json"
        self.logger.info(f"Création de la crew avec log dans {output_log_file}")
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_log_file=str(output_log_file),
            step_callback=self.step_callback,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
