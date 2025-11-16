
def create_prompts(team_name="Southern Illinois", rank=180, stats_snippet=""):
    """
    Generates the positive and negative prompt variations for the framing bias test.
    The stats_snippet must be included in the prompt for the LLM to analyze the data.
    """

    # 1. Define the Ground Truth Snippet (The Facts)
    stats_snippet = f"""
    Team Statistics ({team_name}, Rank {rank}):
    Offensive Efficiency (ADJOE): 106.1
    Defensive Efficiency (ADJDE): 107.7
    Offensive Rebounding (ORB): 30.3
    Defensive Rebounding (DRB): 28.0
    """

    # 2. Define the Prompts
    prompt_positive = f"""
    {stats_snippet}

    Based on these statistics, write a one-paragraph narrative highlighting the team's 
    strengths and identifying key opportunities for breakthrough improvement next season.
    """

    prompt_negative = f"""
    {stats_snippet}

    Based on these statistics, write a one-paragraph narrative focusing on the team's 
    main weaknesses and identifying areas that require immediate correction next season.
    """

    return {
        'positive': prompt_positive.strip(),
        'negative': prompt_negative.strip()
    }

if __name__ == '__main__':
    prompts = create_prompts()
    print("--- Positive Prompt ---")
    print(prompts['positive'])
    print("\n--- Negative Prompt ---")
    print(prompts['negative'])
