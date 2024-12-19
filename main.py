from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv 
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

web_agent.print_response("what is ai agent")