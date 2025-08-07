from crewai import Crew, Process
from agents import research_agent, content_creator_agent, qa_agent, project_manager_agent
from tasks import create_research_task, create_content_creation_task, create_qa_task, create_project_management_task

def simple_crew_example():
    """
    A simple example to demonstrate basic CrewAI functionality
    """
    print("🤖 Simple CrewAI Example - AI Technology Analysis")
    print("=" * 50)
    
    topic = "Artificial Intelligence in Healthcare"
    
    # Create a simple crew with just research and content creation
    research_task = create_research_task(topic)
    content_task = create_content_creation_task(topic)
    
    # Set task dependency
    content_task.context = [research_task]
    
    # Create a simple crew
    simple_crew = Crew(
        agents=[research_agent, content_creator_agent],
        tasks=[research_task, content_task],
        process=Process.sequential,
        verbose=1
    )
    
    # Execute
    result = simple_crew.kickoff()
    
    print("\n" + "=" * 50)
    print("✅ Simple example completed!")
    print("=" * 50)
    print(f"\nResult:\n{result}")

def parallel_crew_example():
    """
    Example of parallel processing with multiple independent tasks
    """
    print("🔄 Parallel CrewAI Example - Multiple Topics")
    print("=" * 50)
    
    # Create multiple independent research tasks
    topics = [
        "Machine Learning Trends 2024",
        "Blockchain Technology Applications",
        "Quantum Computing Developments"
    ]
    
    tasks = []
    for topic in topics:
        task = create_research_task(topic)
        tasks.append(task)
    
    # Create crew with parallel processing
    parallel_crew = Crew(
        agents=[research_agent] * 3,  # Use multiple instances of research agent
        tasks=tasks,
        process=Process.sequential,  # Note: CrewAI currently supports sequential processing
        verbose=1
    )
    
    # Execute
    result = parallel_crew.kickoff()
    
    print("\n" + "=" * 50)
    print("✅ Parallel example completed!")
    print("=" * 50)
    print(f"\nResult:\n{result}")

if __name__ == "__main__":
    print("Choose an example to run:")
    print("1. Simple Crew Example (Research + Content Creation)")
    print("2. Parallel Crew Example (Multiple Research Tasks)")
    print("3. Full Workflow (All agents)")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        simple_crew_example()
    elif choice == "2":
        parallel_crew_example()
    elif choice == "3":
        from crew_main import run_content_creation_project
        topic = input("Enter topic for full workflow: ")
        run_content_creation_project(topic)
    else:
        print("Invalid choice. Running simple example...")
        simple_crew_example()
