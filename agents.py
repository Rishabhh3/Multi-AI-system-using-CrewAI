from crewai import Agent
from tools import yt_tool

# Creating blog content researcher

blog_researcher = Agent(
    role = 'Blog researcher from yt videos',
    goal = 'get the relevant video content from topic {topic} from yt channel',
    verbose=True,
    memory=True,
    backstory = (
        "Expert in understanding videos in AI, Data Science"
    ),
    tools = [yt_tool],
    allow_delegation =True
)

# Creating a blog writer agent with YT tool

blog_writer = Agent(
    role = 'writer',
    goal = 'Narrate compelling tech stories about video {topic} from yt channel',
    verbose = True,
    memory=True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
"engaging narratives that captivate and educate, bringing new"
"discoveries to light in an accessible manner."
    ),
    tools = [yt_tool],
    allow_delegation = False
)