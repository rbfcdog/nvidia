# Build the crew
crew = Crew(
    agents=[
        executor_agent,
        analyst_agent,
        network_specialist,
        web_specialist,
        defense_specialist,
        compiler_agent
    ],
    tasks=[
        task_recon,
        task_analyze,
        task_network,
        task_web,
        task_defense,
        task_compile
    ],
    process=Process.sequential,  # Ensure order: scan → analyze → specialize → compile
    llm=llm,
    verbose=True
)

# Execute the crew
result = crew.kickoff()

print("\n\n✅ Final Report Generated:")
print(result)