from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchRun

def calculator(input: str) -> str:
    try:
        return str(eval(input))
    except Exception:
        return "Error in calculation."

search_tool = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Search",
        func=search_tool.run,
        description="Useful for searching general knowledge or news"
    ),
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for math or numeric calculations"
    )
]