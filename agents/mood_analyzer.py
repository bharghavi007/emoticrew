from crewai import Agent

mood_analyzer = Agent(
    role="Mood Analyzer",
    goal="Analyze the user's text to determine emotional tone or mood",
    backstory="You are a mood analysis expert trained in emotional AI. You detect user emotions from their messages.",
    verbose=True,
    allow_delegation=True
)

