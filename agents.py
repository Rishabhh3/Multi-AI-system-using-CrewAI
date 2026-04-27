from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
# groq_api_key = os.getenv("GROQ_API_KEY")

from crewai import Agent

# creating llm
'''llm = ChatGroq(
    groq_api_key = groq_api_key,
    model="llama-3.2-90b-text-preview",
    temperature=0.7
)'''

# Creating blog content researcher

blog_researcher = Agent(
    role = 'Blog researcher from yt videos',
    goal = 'get the relevant video content from topic {topic} from yt channel',
    verbose=True,
    memory=False, # if true it used openAI
    backstory = (
        "Expert in understanding videos in AI, Data Science"
    ),
    llm = 'groq/llama-3.1-8b-instant',
    allow_delegation =False
)

# Creating a blog writer agent with YT tool

blog_writer = Agent(
    role = 'writer',
    goal = 'Narrate compelling tech stories about video {topic} from yt channel',
    verbose = True,
    memory=False,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
"engaging narratives that captivate and educate, bringing new"
"discoveries to light in an accessible manner."
    ),
    llm = 'groq/llama-3.1-8b-instant',
    allow_delegation = False
)