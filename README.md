

# Task 08: Bias Detection in LLM Data Narratives

This repository contains the documentation and deliverables for Research Task 08, a controlled experiment designed to detect **Framing Bias** in Large Language Model (LLM) generated narratives.

The core objective was to test whether an LLM would interpret the same quantitative data differently based on a simple change in the user's prompt (i.e., asking for "strengths" vs. "weaknesses").

## Key Finding

The experiment successfully detected **Framing Bias** and **Selection Bias**. When prompted with a **positive frame**, the LLM exclusively focused on the team's offensive strengths. When prompted with a **negative frame**, it exclusively focused on the team's defensive weaknesses. The LLM consistently **cherry-picked** statistics to align with the prompt's implied hypothesis.

## Repository Contents

| Directory/File | Description |
| :--- | :--- |
| **`REPORT.md`** | The final report detailing the methodology, results, bias catalogue, and mitigation strategies. **(The primary deliverable)** |
| **`analysis/`** | Contains the quantitative evidence of bias, including the **`bias_visualization.png`** chart and the **`summary_table.md`** of content focus. |
| **`prompts/`** | Stores the two critical prompt variations (**Positive** and **Negative**) used in the experiment. |
| **`results/`** | Contains the simulated raw LLM narrative outputs collected during the data collection phase. |
| **`code/`** | Minimal Python scripts used for design, simulation, and analysis validation: `experiment_design.py`, `run_experiment.py`, and `validate_claims.py`. |

## Experimental Setup

* **Hypothesis:** Framing bias will lead to selection bias in narratives.
* **Data Source:** `cbb25.csv` (College Basketball Statistics).
* **Entity Analyzed:** **Southern Illinois (Rank 180)** (chosen for its balanced profile of both clear strengths and clear weaknesses).
* **Method:** A minimally controlled experiment testing two framing conditions against one statistical snippet.

## How to Reproduce the Findings

1.  **Review Prompts:** Examine the prompts in the `prompts/` directory to understand the simple difference in framing.
2.  **View Results:** Read the simulated narratives in the `results/` directory to see the clear contrast in content focus.
3.  **Check Analysis:** View the `analysis/bias_visualization.png` chart to see the quantitative proof of the $100\%$ split in content focus.
4.  **Review Code:** The Python files in `code/` document the technical steps taken for prompt creation, simulation, and bias validation.
