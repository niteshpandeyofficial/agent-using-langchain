from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from tools import *

tools = [search_tool, get_weather_data]

agent=create_agent(
    model=ChatOpenAI(),
    tools=tools,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the search tool for web searches and "
        "the weather tool to answer weather questions."
    )
)

# noinspection PyTypeChecker
result = agent.invoke(
    {
    "messages": [
        {
            "role": "user",
            "content": "Find the capital of Madhya Pradesh, then find it's current temperature"
        }
    ]
    })

print(result["messages"][-1].content)
