from crewai import Crew, Task
from agents.mood_analyzer import mood_analyzer
from agents.companion import companion
from agents.selfcare_recommender import selfcare_recommender
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

def run_crew(user_input):
    task1 = Task(
        description=f"Analyze the following message and detect mood: '{user_input}'",
        expected_output="A very short phrase like 'You seem anxious.'",
        agent=mood_analyzer
    )

    task2 = Task(
        description="Give a short supportive message tailored to the mood.",
        expected_output="Something like 'You're doing your best, and that matters.'",
        agent=companion
    )

    task3 = Task(
        description="Suggest a brief self-care tip appropriate for the mood.",
        expected_output="One actionable item like 'Take a 5-minute stretch break.'",
        agent=selfcare_recommender
    )

    crew = Crew(
        agents=[mood_analyzer, companion, selfcare_recommender],
        tasks=[task1, task2, task3],
        llm=llm,
        verbose=True
    )

    return crew.kickoff()  
