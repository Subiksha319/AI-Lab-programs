# Experiment 10: Prompt Design and Evaluation Using Generative AI

import pandas as pd

# Read the input CSV file
df = pd.read_csv("experiment_10_prompt_evaluation.csv")


# Function to evaluate prompt
def evaluate_prompt(prompt):

    text = prompt.lower()

    features = {
        "Role": any(word in text for word in ["act as", "you are"]),

        "Context": any(word in text for word in [
            "student", "manager", "college", "project", "report"
        ]),

        "Clear task": any(word in text for word in [
            "explain", "draft", "review", "summarize", "compare"
        ]),

        "Constraints": any(word in text for word in [
            "words", "bullet", "under", "three", "five"
        ]),

        "Output format": any(word in text for word in [
            "table", "subject", "bullet points", "example"
        ])
    }

    return sum(features.values()), features


# Evaluate all prompts
print("----- PROMPT DESIGN AND EVALUATION -----")

for _, row in df.iterrows():

    weak_score, _ = evaluate_prompt(row["Weak_Prompt"])

    improved_score, features = evaluate_prompt(
        row["Improved_Prompt"]
    )

    print(f"\nPrompt ID: {row['Prompt_ID']} | Task: {row['Task']}")

    print(f"Weak prompt score     : {weak_score}/5")

    print(f"Improved prompt score : {improved_score}/5")

    print("Satisfied features    :",
          ", ".join(k for k, v in features.items() if v))

    print("Evaluation            :",
          "Improved" if improved_score > weak_score else "Needs review")


# Calculate average scores
df["Weak_Score"] = df["Weak_Prompt"].apply(
    lambda x: evaluate_prompt(x)[0]
)

df["Improved_Score"] = df["Improved_Prompt"].apply(
    lambda x: evaluate_prompt(x)[0]
)


# Display overall summary
print("\n----- OVERALL SUMMARY -----")

print("Average weak prompt score    :",
      round(df["Weak_Score"].mean(), 2))

print("Average improved prompt score:",
      round(df["Improved_Score"].mean(), 2))

print("\nEvaluation completed. This is a rule-based prompt-quality checklist, not an LLM evaluation.")