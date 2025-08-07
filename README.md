# CrewAI Multiple Agents Project

This project demonstrates how to use CrewAI to create and coordinate multiple AI agents using NVIDIA's API for language model inference.

## Project Structure

```
nvidia/
├── .env                    # Environment variables (API keys)
├── llm_config.py          # LLM configuration for NVIDIA API
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
├── crew_main.py           # Main crew workflow
├── examples.py            # Example implementations
├── allan/
│   └── chamada_api.py     # Original NVIDIA API call example
└── README.md              # This file
```

## Features

### Multiple Agent Types

1. **Research Agent**: Conducts thorough research and gathers information
2. **Content Creator Agent**: Creates engaging content based on research
3. **Quality Assurance Agent**: Reviews and improves content quality
4. **Project Manager Agent**: Coordinates workflow and manages the project

### Key Capabilities

- **Sequential Workflow**: Tasks are executed in logical order with dependencies
- **Context Sharing**: Agents can access outputs from previous tasks
- **NVIDIA API Integration**: Uses NVIDIA's Llama model via their API
- **Flexible Task Creation**: Easy to create new tasks and workflows
- **Detailed Logging**: Comprehensive output for monitoring progress

## Setup Instructions

### 1. Environment Setup

Make sure you have Python 3.8+ installed, then install dependencies:

```bash
pip install crewai langchain langchain-openai python-dotenv
```

### 2. API Configuration

The project is already configured to use your NVIDIA API key. The configuration is in `.env`:

```
NVIDIA_API_KEY=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
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

### 3. Running the Project

#### Full Workflow Example
```bash
python crew_main.py
```
Enter a topic when prompted, and watch as all four agents collaborate to research, create content, review it, and manage the project.

#### Simple Examples
```bash
python examples.py
```
Choose from different example scenarios:
- Simple crew with 2 agents
- Multiple research tasks
- Full workflow

#### Individual Components
```bash
# Test just the agents
python -c "from agents import *; print('Agents loaded successfully!')"

# Test LLM configuration
python -c "from llm_config import get_nvidia_llm; llm = get_nvidia_llm(); print('LLM configured!')"
```

## Usage Examples

### Basic Usage

```python
from crew_main import run_content_creation_project

# Run a complete content creation workflow
result = run_content_creation_project("Artificial Intelligence in Healthcare")
```

### Custom Crew Creation

```python
from crewai import Crew, Process
from agents import research_agent, content_creator_agent
from tasks import create_research_task, create_content_creation_task

# Create custom workflow
topic = "Your Topic Here"
research_task = create_research_task(topic)
content_task = create_content_creation_task(topic)

content_task.context = [research_task]

crew = Crew(
    agents=[research_agent, content_creator_agent],
    tasks=[research_task, content_task],
    process=Process.sequential
)

result = crew.kickoff()
```

## Agent Roles and Responsibilities

### 🔍 Research Agent
- Gathers comprehensive information
- Identifies key concepts and trends
- Finds credible sources and statistics
- Analyzes current developments

### ✍️ Content Creator Agent  
- Transforms research into engaging content
- Structures information effectively
- Creates compelling narratives
- Optimizes for readability

### 🔍 Quality Assurance Agent
- Reviews content for accuracy
- Checks grammar and style
- Ensures coherence and flow
- Provides improvement suggestions

### 📋 Project Manager Agent
- Coordinates team activities
- Monitors progress and timelines
- Ensures objectives are met
- Provides project summaries

## Workflow Process

1. **Research Phase**: Research agent gathers comprehensive information
2. **Content Creation**: Content creator transforms research into engaging content
3. **Quality Review**: QA agent reviews and improves the content
4. **Project Management**: PM agent coordinates and summarizes the entire process

## Customization Options

### Adding New Agents
```python
# In agents.py
new_agent = Agent(
    role="Your Agent Role",
    goal="Agent's specific goal",
    backstory="Agent's background and expertise",
    llm=llm
)
```

### Creating New Tasks
```python
# In tasks.py
def create_custom_task(parameters):
    return Task(
        description="Task description with specific requirements",
        agent=your_agent,
        expected_output="Expected output format"
    )
```

### Modifying LLM Settings
```python
# In llm_config.py - adjust these parameters:
# - temperature: Controls randomness (0.0 - 1.0)
# - max_tokens: Maximum response length
# - model: NVIDIA model to use
```

## Troubleshooting

### Common Issues

1. **API Key Issues**: Make sure your NVIDIA API key is valid and has sufficient credits
2. **Module Import Errors**: Ensure all dependencies are installed in the correct environment
3. **Rate Limiting**: NVIDIA API may have rate limits - add delays if needed

### Debug Mode
Enable detailed logging by setting `verbose=2` in crew configuration:

```python
crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=2  # Maximum verbosity
)
```

## Next Steps

1. **Experiment with different topics** to see how agents adapt
2. **Add more specialized agents** for specific domains
3. **Implement tools** for agents to access external APIs or databases
4. **Create parallel workflows** for independent tasks
5. **Add memory and learning** capabilities to agents

## Contributing

Feel free to extend this project by:
- Adding new agent types
- Creating specialized tasks
- Implementing external tool integrations
- Improving error handling and logging

---

This project demonstrates the power of multi-agent AI systems and how they can collaborate to achieve complex goals. Each agent brings specialized skills to create a comprehensive workflow that's greater than the sum of its parts.