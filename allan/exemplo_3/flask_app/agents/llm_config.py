import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_nvidia_llm():
    """
    Configure and return optimized NVIDIA LLM for CrewAI agents
    """
    from crewai.llm import LLM
    
    # Optimized configuration for faster responses
    return LLM(
        model="nvidia/llama-3.3-nemotron-super-49b-v1.5",
        api_key=os.getenv("NVIDIA_API_KEY"),
        base_url=os.getenv("NVIDIA_BASE_URL"),
        temperature=0.3,  # Reduzido para respostas mais determinísticas
        max_tokens=2048,  # Reduzido de 4096 para respostas mais concisas
        timeout=60,  # Timeout de 60 segundos
        max_retries=2  # Máximo 2 tentativas
    )