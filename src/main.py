import os
from dotenv import load_dotenv
from langchain.agents import create_agent
load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

def get_weather(city: str) -> str:
    """Get weather for a give city"""
    return f"Weather of {city} is sunny!"

agent = create_agent(
    model = "google_genai:gemini-3.5-flash-lite",
    tools = [get_weather],
    system_prompt="You are helpful assistant!"
)

result = agent.invoke(
    {"messages": [{"role":"user","content": "What is the weather in delhi?"}]}
)

print(result["messages"][-1].text)

