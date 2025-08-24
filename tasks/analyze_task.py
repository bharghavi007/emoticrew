from crewai import Task

def create_analyze_task(user_input, agent):
    return Task(
        description=f"Analyze this text: '{user_input}' and respond with:\n"
                    "1. Mood detected\n"
                    "2. Supportive message\n"
                    "3. Self-care suggestion",
        expected_output="A friendly response from all agents working together to support the user's mental state.",
        agent=agent
    )

