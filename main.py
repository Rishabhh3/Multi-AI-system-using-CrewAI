# This is from where the execution will start

from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writer_task
import traceback

# Forming tech crew with enhanced configuration
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writer_task],
    process=Process.sequential, # Optional: Sequential task execution
    memory = False,
    cache = True,
    max_rpm = 100,
)

# Start task execution with enhanced feedback

try:
    result = crew.kickoff(inputs={'topic': 'AI vs ML vs Datascience'})
    print(result)
except Exception as e:
    print("Crew kickoff failed:", repr(e))
    traceback.print_exc()
    raise