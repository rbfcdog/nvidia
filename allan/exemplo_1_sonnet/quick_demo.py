#!/usr/bin/env python3
"""
Quick demo script to show CrewAI agents in action
This runs a minimal example to demonstrate the system
"""

from crewai import Crew, Process, Task, Agent
from llm_config import get_nvidia_llm

def quick_demo():
    """Run a quick demonstration of CrewAI with NVIDIA's API"""
    print("🚀 CrewAI Quick Demo")
    print("=" * 50)
    
    # Get LLM
    llm = get_nvidia_llm()
    
    # Create a simple agent
    demo_agent = Agent(
        role="AI Assistant",
        goal="Provide helpful and concise information",
        backstory="You are a knowledgeable AI assistant that provides clear, accurate information.",
        verbose=True,
        llm=llm
    )
    
    # Create a simple task
    demo_task = Task(
        description="Qual o nome do melhor jogador de futebol de todos os tempos ?",
        agent=demo_agent,
        expected_output="A brief, clear explanation of CrewAI"
    )
    
    # Create crew
    demo_crew = Crew(
        agents=[demo_agent],
        tasks=[demo_task],
        process=Process.sequential,
        verbose=1
    )
    
    print("Starting demo...")
    print("-" * 30)
    
    try:
        result = demo_crew.kickoff()
        print("\n" + "=" * 50)
        print("✅ Demo completed successfully!")
        print("=" * 50)
        print(f"\nResult: {result}")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {str(e)}")

if __name__ == "__main__":
    quick_demo()
