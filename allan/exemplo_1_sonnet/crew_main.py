from crewai import Crew, Process
from agents import research_agent, content_creator_agent, qa_agent, project_manager_agent
from tasks import create_research_task, create_content_creation_task, create_qa_task, create_project_management_task

def create_content_crew(topic):
    """
    Create and configure a CrewAI crew for content creation workflow
    """
    
    # Create tasks for the given topic
    research_task = create_research_task(topic)
    content_task = create_content_creation_task(topic)
    qa_task = create_qa_task()
    pm_task = create_project_management_task(topic)
    
    # Set up task dependencies
    content_task.context = [research_task]  # Content creation depends on research
    qa_task.context = [content_task]        # QA depends on content creation
    pm_task.context = [research_task, content_task, qa_task]  # PM oversees all
    
    # Create the crew
    crew = Crew(
        agents=[research_agent, content_creator_agent, qa_agent, project_manager_agent],
        tasks=[research_task, content_task, qa_task, pm_task],
        process=Process.sequential,  # Tasks will be executed in sequence
        verbose=True  # Maximum verbosity for detailed output
    )
    
    return crew

def run_content_creation_project(topic):
    """
    Run the complete content creation project
    """
    print(f"🚀 Starting content creation project for topic: {topic}")
    print("=" * 60)
    
    # Create the crew
    crew = create_content_crew(topic)
    
    # Execute the workflow
    try:
        result = crew.kickoff()
        
        print("\n" + "=" * 60)
        print("✅ Project completed successfully!")
        print("=" * 60)
        print("\n📋 Final Result:")
        print(result)
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error during project execution: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    topic = input("Enter the topic you want to create content about: ")
    
    if topic.strip():
        run_content_creation_project(topic)
    else:
        print("Please provide a valid topic!")
