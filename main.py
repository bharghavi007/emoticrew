from crewai import Crew
from agents.mood_analyzer import mood_analyzer
from agents.companion import companion
from agents.selfcare import selfcare_agent
from tasks.analyze_task import create_analyze_task
import config

def main():
    user_input = "I feel really tired and unmotivated lately. Everything feels dull."

    task = create_analyze_task(user_input, mood_analyzer)

    crew = Crew(
        agents=[mood_analyzer, companion, selfcare_agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()
    print("\n🤖 Final Response:\n", result)


if __name__ == "__main__":
    main()


