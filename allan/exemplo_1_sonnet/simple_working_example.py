#!/usr/bin/env python3
"""
Simple working example of CrewAI with NVIDIA API
This uses a direct approach that should work reliably
"""

import requests
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# Load environment variables
load_dotenv()

class SimpleNvidiaLLM:
    """Simple LLM wrapper for NVIDIA API that works with CrewAI"""
    
    def __init__(self):
        self.api_key = os.getenv("NVIDIA_API_KEY")
        self.base_url = os.getenv("NVIDIA_BASE_URL")
        self.model = "nvidia/llama-3.3-nemotron-super-49b-v1.5"
    
    def __call__(self, messages, **kwargs):
        """Make this callable like CrewAI expects"""
        return self.generate_response(messages, **kwargs)
    
    def generate_response(self, messages, **kwargs):
        """Generate response from NVIDIA API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }
        
        # Format messages properly
        if isinstance(messages, str):
            formatted_messages = [{"role": "user", "content": messages}]
        elif isinstance(messages, list):
            formatted_messages = messages
        else:
            formatted_messages = [{"role": "user", "content": str(messages)}]
        
        payload = {
            "model": self.model,
            "messages": formatted_messages,
            "max_tokens": kwargs.get("max_tokens", 512),
            "temperature": kwargs.get("temperature", 0.7)
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"API Error: {response.status_code} - {response.text}"
                
        except Exception as e:
            return f"Request Error: {str(e)}"

def run_simple_example():
    """Run a simple CrewAI example"""
    print("🚀 Simple CrewAI with NVIDIA API Example")
    print("=" * 50)
    
    # Create custom LLM
    nvidia_llm = SimpleNvidiaLLM()
    
    # Test the LLM directly first
    print("Testing direct API call...")
    test_response = nvidia_llm.generate_response("What is artificial intelligence?")
    print(f"Direct API Response: {test_response[:100]}...")
    
    print("\nNow testing with CrewAI...")
    
    # Create a simple agent
    simple_agent = Agent(
        role="AI Researcher", 
        goal="Provide accurate information about AI topics",
        backstory="You are an AI researcher with deep knowledge of artificial intelligence.",
        verbose=True,
        llm=nvidia_llm  # Use our custom LLM
    )
    
    # Create a simple task
    simple_task = Task(
        description="Explain what machine learning is in exactly 2 sentences.",
        agent=simple_agent,
        expected_output="A clear 2-sentence explanation of machine learning"
    )
    
    # Create crew
    crew = Crew(
        agents=[simple_agent],
        tasks=[simple_task],
        process=Process.sequential,
        verbose=1
    )
    
    try:
        print("Running CrewAI workflow...")
        result = crew.kickoff()
        print("\n" + "=" * 50)
        print("✅ Success!")
        print("=" * 50)
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    run_simple_example()
