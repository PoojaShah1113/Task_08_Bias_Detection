import json
import time

def simulate_llm_response(prompt_type):
    """Simulates the LLM generating a biased response."""
    if prompt_type == 'positive':
        return """
        The Southern Illinois program shows significant promise, driven entirely by their offensive firepower. 
        Their strong Adjusted Offensive Efficiency (ADJOE) of 106.1 is a clear strength, coupled with an excellent 
        Offensive Rebounding (ORB) rate of 30.3, which generates crucial second-chance points. The path to a 
        breakthrough next season lies in maximizing these successful offensive tendencies. (NOTE: Defensive metrics ignored)
        """
    elif prompt_type == 'negative':
        return """
        The primary obstacle facing the Southern Illinois team is their subpar performance on the defensive end of the court. 
        Their defensive weakness is highlighted by a poor Adjusted Defensive Efficiency (ADJDE) of 107.7. Furthermore, 
        the team struggles significantly with its Defensive Rebounding (DRB), securing only 28.0 percent of available 
        defensive rebounds. Addressing these urgent defensive lapses is the top priority for correction. (NOTE: Offensive metrics ignored)
        """
    return "Error: Unknown prompt type."


def run_simulated_experiment():
    """Simulates the collection of a minimal set of data."""
    results = []
    
    # Run two samples (minimal required)
    for i in range(1, 3):
        # Positive Sample
        results.append({
            'model': 'Simulated_Gemini_1.0',
            'prompt_condition': 'Positive Framing',
            'sample_id': i,
            'raw_response': simulate_llm_response('positive').strip(),
            'timestamp': time.time()
        })
        
        # Negative Sample
        results.append({
            'model': 'Simulated_Gemini_1.0',
            'prompt_condition': 'Negative Framing',
            'sample_id': i,
            'raw_response': simulate_llm_response('negative').strip(),
            'timestamp': time.time()
        })

    # Save results to simulate the logging process (to the results/ directory)
    with open('results/raw_responses_simulated.json', 'w') as f:
        json.dump(results, f, indent=4)
    
    print(f"Successfully simulated and logged {len(results)} responses to results/raw_responses_simulated.json")

if __name__ == '__main__':
    # Ensure the results directory exists before running
    import os
    if not os.path.exists('results'):
        os.makedirs('results')
    run_simulated_experiment()
