from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    """Lookup current local time for a city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model="gemini-flash-latest",
    name="root_agent",
    description="A global time assistant that provides the current local time for requested cities.",
    instruction=(
        "You are a helpful assistant that answers questions about the current local time in cities. "
        "Use the get_current_time tool for city time lookup. If the city is ambiguous or missing, ask the user to clarify."
    ),
    tools=[get_current_time],
)