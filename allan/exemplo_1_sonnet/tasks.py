from crewai import Task
from agents import research_agent, content_creator_agent, qa_agent, project_manager_agent

def create_research_task(topic):
    """Create a research task for the given topic"""
    return Task(
        description=f"""
        Conduct comprehensive research on the topic: {topic}
        
        Your research should include:
        1. Key concepts and definitions
        2. Current trends and developments
        3. Important statistics and data points
        4. Main challenges and opportunities
        5. Expert opinions and insights
        6. Recent news and updates
        
        Provide a detailed research report with credible sources and references.
        """,
        agent=research_agent,
        expected_output="A comprehensive research report with key findings, statistics, and references"
    )

def create_content_creation_task(topic):
    """Create a content creation task"""
    return Task(
        description=f"""
        Based on the research findings, create engaging and informative content about: {topic}
        
        Your content should:
        1. Be well-structured with clear headings and sections
        2. Include an engaging introduction
        3. Present information in an accessible way
        4. Include relevant examples and case studies
        5. Have a compelling conclusion
        6. Be optimized for readability
        
        Create content that would be suitable for a professional blog post or article.
        """,
        agent=content_creator_agent,
        expected_output="A well-structured, engaging article or blog post with clear sections and compelling content"
    )

def create_qa_task():
    """Create a quality assurance task"""
    return Task(
        description="""
        Review and improve the content created by the Content Creator.
        
        Your review should focus on:
        1. Accuracy of information
        2. Clarity and coherence
        3. Grammar and style
        4. Structure and flow
        5. Completeness of coverage
        6. Engagement factor
        
        Provide specific feedback and suggestions for improvement.
        Create a final, polished version of the content.
        """,
        agent=qa_agent,
        expected_output="A comprehensive review with specific feedback and a final, polished version of the content"
    )

def create_project_management_task(topic):
    """Create a project management task"""
    return Task(
        description=f"""
        Oversee the entire content creation project for the topic: {topic}
        
        Your responsibilities include:
        1. Ensuring all team members understand their roles
        2. Monitoring progress and timeline
        3. Coordinating between team members
        4. Ensuring project objectives are met
        5. Providing final project summary and recommendations
        
        Create a comprehensive project summary that includes insights from all team members.
        """,
        agent=project_manager_agent,
        expected_output="A comprehensive project summary with timeline, key achievements, and recommendations for future projects"
    )
