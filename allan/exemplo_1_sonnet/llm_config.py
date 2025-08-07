import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_nvidia_llm():
    """
    Configure and return NVIDIA LLM for CrewAI agents using CrewAI's LLM class
    """
    from crewai.llm import LLM
    
    # CrewAI's LLM class with custom configuration
    return LLM(
        model="openai/gpt-3.5-turbo",  # Using a supported model format for now
        api_key=os.getenv("NVIDIA_API_KEY"),
        base_url=os.getenv("NVIDIA_BASE_URL"),
        temperature=0.7,
        max_tokens=1024
    )

def get_nvidia_custom_llm():
    """
    Custom LLM implementation for NVIDIA API
    """
    class NvidiaCustomLLM:
        def __init__(self):
            self.api_key = os.getenv("NVIDIA_API_KEY")
            self.base_url = os.getenv("NVIDIA_BASE_URL")
            self.model = "meta/llama-4-maverick-17b-128e-instruct"
            
        def __call__(self, prompt, **kwargs):
            return self.generate(prompt, **kwargs)
            
        def generate(self, prompt, **kwargs):
            import requests
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json"
            }
            
            # Handle different prompt formats
            if isinstance(prompt, str):
                messages = [{"role": "user", "content": prompt}]
            elif isinstance(prompt, list):
                messages = prompt
            else:
                messages = [{"role": "user", "content": str(prompt)}]
            
            payload = {
                "model": self.model,
                "messages": messages,
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
                    content = response.json()["choices"][0]["message"]["content"]
                    return content
                else:
                    raise Exception(f"API call failed: {response.status_code} - {response.text}")
                    
            except Exception as e:
                print(f"Error calling NVIDIA API: {e}")
                return f"Error: Unable to generate response - {str(e)}"
    
    return NvidiaCustomLLM()

def get_langchain_nvidia_llm():
    """
    LangChain compatible NVIDIA LLM
    """
    from langchain_openai import ChatOpenAI
    
    return ChatOpenAI(
        model="gpt-3.5-turbo",  # Will be overridden by base_url
        openai_api_key=os.getenv("NVIDIA_API_KEY"),
        openai_api_base=os.getenv("NVIDIA_BASE_URL"),
        temperature=0.7,
        max_tokens=1024
    )
