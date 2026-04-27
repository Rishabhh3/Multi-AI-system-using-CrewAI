from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool

# Research task
research_task = Task(
    description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel."
    ),

    expected_output = "A comprehensive 3 paragraphs long report based on the {topic} of video and create the content for the blog",
    tools=[yt_tool],
    agent=blog_researcher,
)

# write task
writer_task = Task(
    description=(
    "get the info of the youtube video from the channel @krishnaik06 topic {topic}"
    ),
    expected_output = "Summarize the info from the youtube channel video on topic {topic} ",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution = False, # if True both the agents will parallely but I dont want it now
    output_file='new_blog_post.md' # example of output customization
)