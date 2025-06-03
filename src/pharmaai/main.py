#!/usr/bin/env python
import sys
from tabnanny import verbose
import warnings

from datetime import datetime

from pharmaai.crew import Pharmaai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Demander la question à l'utilisateur
    question = input("Quelle est votre question pharmaceutique ? ")
    inputs = {
        'question_pharmacienne': question,
        'current_year': str(datetime.now().year)
    }
    try:
        Pharmaai().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Demander la question à l'utilisateur
    question = input("Quelle est votre question pharmaceutique pour l'entraînement ? ")
    inputs = {
        'question_pharmacienne': question,
        'current_year': str(datetime.now().year)
    }
    try:
        Pharmaai().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Pharmaai().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    # Demander la question à l'utilisateur
    question = input("Quelle est votre question pharmaceutique pour le test ? ")
    inputs = {
        'question_pharmacienne': question,
        'current_year': str(datetime.now().year)
    }
    try:
        Pharmaai().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
