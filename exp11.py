
# Experiment 11: Role-Based, Zero-Shot,
# One-Shot and Few-Shot Prompting

import pandas as pd

# Read CSV file
df = pd.read_csv("experiment_11_prompting_techniques.csv")

# Positive and negative words
positive_words = {
    "quick", "perfectly", "excellent",
    "helpful", "love", "early", "great"
}

negative_words = {
    "poor", "dull", "stopped",
    "broken", "slow", "unavailable"
}

# Sentiment analysis function
def sentiment_demo(sentence):
    words = set(
        sentence.lower()
        .replace(".", "")
        .replace(",", "")
        .split()
    )

    score = len(words & positive_words) - len(words & negative_words)

    return (
        "Positive" if score > 0
        else "Negative" if score < 0
        else "Neutral"
    )


# Construct prompt
def construct_prompt(row):

    role = row["Role"]
    task = row["Task"]
    text = row["Input_Text"]
    technique = row["Technique"]

    if technique == "Zero-Shot":
        return f"You are a {role}. {task}: {text}"

    if technique == "One-Shot":
        return (
            f"You are a {role}. {task}. Example: "
            f"{row['Example_Input']} -> "
            f"{row['Example_Output']}. New input: {text}"
        )

    if technique == "Few-Shot":
        return (
            f"You are a {role}. {task}. Examples: "
            "Excellent service -> Positive; "
            "Poor quality -> Negative. "
            f"New input: {text}"
        )

    return f"Act as a {role}. {task}: {text}"


# Display results
print("----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----")

for _, row in df.iterrows():

    prompt = construct_prompt(row)

    if "sentiment" in row["Task"].lower():
        response = sentiment_demo(row["Input_Text"])

    elif "priority" in row["Task"].lower():
        response = (
            "High"
            if "unavailable" in row["Input_Text"].lower()
            else "Low"
        )

    else:
        response = (
            "Suggested rewrite: Please share the project "
            "file at your earliest convenience."
        )

    print(
        f"\nID: {row['Example_ID']} | "
        f"Technique: {row['Technique']}"
    )

    print("Constructed prompt:", prompt)

    print("Python demonstration response:", response)


print(
    "\nDemonstration completed. Responses use predefined "
    "Python rules, not a live LLM."
)
