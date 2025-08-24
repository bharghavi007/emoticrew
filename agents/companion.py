from crewai import Agent

companion = Agent(
    role="Companion",
    goal="Provide supportive, empathetic responses to user’s emotional state",
    backstory="You are a virtual friend who listens and supports users in emotional distress with empathy.",
    verbose=True,
    allow_delegation=True
)

