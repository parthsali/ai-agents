from phi.agent import Agent
from phi.tools.github import GithubTools
from dotenv import load_dotenv
from phi.model.groq import Groq

load_dotenv()

agent = Agent(
    name="GitHub Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "You are just here retrive data from GitHub, it could be anything from issues, pull requests, repo details, etc.",
    ],
    tools=[GithubTools()],
    show_tool_calls=True,
)
agent.print_response("create a issue on this repository : forrealdeveloper/Portfolio saying need more details", markdown=True)
