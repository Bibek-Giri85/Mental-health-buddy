from crewai import Agent

mood_analyzer = Agent(
    role="Mood Analyzer",
    goal="Identify the user's emotional tone from a message",
    backstory="You analyze text and classify it emotionally—happy, sad, anxious, etc.",
    verbose=True
)
