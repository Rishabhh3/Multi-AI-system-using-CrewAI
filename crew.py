# This is from where the execution will start

from crewai import crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writer_task

# Forming tech crew with enhanced configuration
crew = crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writer_task],
    process=Process.sequential, # Optional: Sequential task execution
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True

)

# Start task execution with enhanced feedback

result = crew.kickoff(inputs = {'topic':'AI vs ML vs Datascience'})
print(result)