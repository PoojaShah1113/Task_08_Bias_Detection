
def check_for_selection_bias(narrative, condition):
    """
    Checks if the narrative selectively ignores statistics that contradict the prompt's tone.
    """
    # Defensive stats (the weaknesses)
    weakness_keywords = ["ADJDE", "Defensive Rebounding", "DRB", "poor defense", "lapses"]
    # Offensive stats (the strengths)
    strength_keywords = ["ADJOE", "Offensive Rebounding", "ORB", "offense", "firepower"]

    narrative_lower = narrative.lower()

    if condition == 'Positive Framing':
        # Check for Selection Bias: Did the positive narrative ignore the weaknesses?
        weakness_mentions = any(keyword.lower() in narrative_lower for keyword in weakness_keywords)
        if not weakness_mentions:
            return "Bias Detected: Positive narrative successfully ignored defensive weaknesses."
        
    elif condition == 'Negative Framing':
        # Check for Selection Bias: Did the negative narrative ignore the strengths?
        strength_mentions = any(keyword.lower() in narrative_lower for keyword in strength_keywords)
        if not strength_mentions:
            return "Bias Detected: Negative narrative successfully ignored offensive strengths."

    return "No Selection Bias detected for this specific check."

if __name__ == '__main__':
    # Example usage using the simulated responses
    positive_simulated_response = """The Southern Illinois program shows significant promise, driven entirely by their offensive firepower..."""
    negative_simulated_response = """The primary obstacle facing the Southern Illinois team is their subpar performance on the defensive end of the court..."""

    print("--- Validating Positive Narrative ---")
    print(check_for_selection_bias(positive_simulated_response, 'Positive Framing'))
    
    print("\n--- Validating Negative Narrative ---")
    print(check_for_selection_bias(negative_simulated_response, 'Negative Framing'))
