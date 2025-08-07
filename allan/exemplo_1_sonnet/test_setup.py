#!/usr/bin/env python3
"""
Simple test script to verify CrewAI setup is working correctly
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import crewai
        print("✅ CrewAI imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import CrewAI: {e}")
        return False
    
    try:
        import langchain
        print("✅ LangChain imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import LangChain: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import python-dotenv: {e}")
        return False
    
    return True

def test_configuration():
    """Test if configuration files are properly set up"""
    print("\n🔧 Testing configuration...")
    
    # Test .env file
    if os.path.exists('.env'):
        print("✅ .env file found")
        from dotenv import load_dotenv
        load_dotenv()
        
        if os.getenv('NVIDIA_API_KEY'):
            print("✅ NVIDIA_API_KEY found in environment")
        else:
            print("❌ NVIDIA_API_KEY not found in environment")
            return False
    else:
        print("❌ .env file not found")
        return False
    
    return True

def test_llm_config():
    """Test LLM configuration"""
    print("\n🤖 Testing LLM configuration...")
    
    try:
        from llm_config import get_nvidia_llm
        llm = get_nvidia_llm()
        print("✅ LLM configuration loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to configure LLM: {e}")
        return False

def test_agents():
    """Test agent creation"""
    print("\n👥 Testing agents...")
    
    try:
        from agents import research_agent, content_creator_agent, qa_agent, project_manager_agent
        print("✅ All agents loaded successfully")
        print(f"   - Research Agent: {research_agent.role}")
        print(f"   - Content Creator: {content_creator_agent.role}")
        print(f"   - QA Agent: {qa_agent.role}")
        print(f"   - Project Manager: {project_manager_agent.role}")
        return True
    except Exception as e:
        print(f"❌ Failed to load agents: {e}")
        return False

def test_tasks():
    """Test task creation"""
    print("\n📝 Testing task creation...")
    
    try:
        from tasks import create_research_task, create_content_creation_task
        
        # Test creating tasks
        research_task = create_research_task("Test Topic")
        content_task = create_content_creation_task("Test Topic")
        
        print("✅ Tasks created successfully")
        print(f"   - Research Task: {research_task.description[:50]}...")
        print(f"   - Content Task: {content_task.description[:50]}...")
        return True
    except Exception as e:
        print(f"❌ Failed to create tasks: {e}")
        return False

def run_quick_test():
    """Run a very quick test with minimal API usage"""
    print("\n🚀 Running quick crew test...")
    
    try:
        from crewai import Crew, Process
        from agents import research_agent
        from tasks import create_research_task
        
        # Create a simple task
        task = create_research_task("Python programming basics")
        
        # Create a minimal crew
        crew = Crew(
            agents=[research_agent],
            tasks=[task],
            process=Process.sequential,
            verbose=1
        )
        
        print("✅ Crew created successfully")
        print("   Note: To run actual inference, use crew.kickoff()")
        print("   This would consume API credits, so we're skipping actual execution")
        
        return True
    except Exception as e:
        print(f"❌ Failed to create crew: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 CrewAI Project Setup Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_configuration,
        test_llm_config,
        test_agents,
        test_tasks,
        run_quick_test
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        if test():
            passed += 1
        else:
            failed += 1
        print()
    
    print("=" * 40)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Your CrewAI project is ready to use.")
        print("\nTo get started:")
        print("  python examples.py      # Run example scenarios")
        print("  python crew_main.py     # Run full workflow")
    else:
        print("⚠️  Some tests failed. Please check the setup.")
        sys.exit(1)

if __name__ == "__main__":
    main()
