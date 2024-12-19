from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="YouTube Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=5Jk8qITsqdM", markdown=True)
