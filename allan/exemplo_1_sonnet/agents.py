from crewai import Agent
from llm_config import get_nvidia_custom_llm

# Get the configured LLM
llm = get_nvidia_custom_llm()

# Research Agent - Gathers information and does research
research_agent = Agent(
    role="Senior Research Analyst",
    goal="Conduct thorough research and gather comprehensive information on any given topic",
    backstory="""You are a meticulous research analyst with years of experience in 
    gathering, analyzing, and synthesizing information from various sources. You have 
    a keen eye for detail and can identify the most relevant and credible information.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Content Creator Agent - Creates engaging content
content_creator_agent = Agent(
    role="Expert Content Creator",
    goal="Create engaging, well-structured, and informative content based on research findings",
    backstory="""You are a talented content creator with expertise in transforming 
    complex research into accessible, engaging content. You understand how to structure 
    information effectively and create compelling narratives that resonate with audiences.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Quality Assurance Agent - Reviews and improves content
qa_agent = Agent(
    role="Quality Assurance Specialist",
    goal="Review, analyze, and improve content quality, ensuring accuracy and coherence",
    backstory="""You are a detail-oriented quality assurance specialist with a strong 
    background in content review and editing. You excel at identifying inconsistencies, 
    errors, and areas for improvement while maintaining the original intent and voice.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Project Manager Agent - Coordinates the workflow
project_manager_agent = Agent(
    role="Project Manager",
    goal="Coordinate team activities, ensure project goals are met, and manage workflow efficiently",
    backstory="""You are an experienced project manager with excellent organizational 
    skills. You understand how to coordinate different team members, manage timelines, 
    and ensure that all project objectives are achieved successfully.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)
