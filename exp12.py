
# Experiment 12: AI-Assisted Generation of Technical Content
# and Python Programs

import pandas as pd
from pathlib import Path

# Read CSV file
df = pd.read_csv("experiment_12_technical_generation.csv")

# Predefined Python templates
templates = {

    "CSV Data Analysis": '''import pandas as pd

def column_average(filename, column):
    data = pd.read_csv(filename)

    if column not in data.columns:
        raise ValueError("Column not found")

    values = pd.to_numeric(data[column], errors="coerce").dropna()

    if values.empty:
        raise ValueError("No numeric values available")

    return round(values.mean(), 2)
''',

    "Temperature Conversion": '''def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be numeric")

    return round((celsius * 9 / 5) + 32, 2)
''',

    "Password Validation": '''def check_password(password):
    checks = {
        "Minimum 8 characters": len(password) >= 8,
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digit": any(c.isdigit() for c in password),
        "Special character": any(not c.isalnum() for c in password)
    }

    for rule, passed in checks.items():
        print(rule, ":", "Pass" if passed else "Fail")

    return all(checks.values())
''',

    "List Statistics": '''def list_statistics(values):
    if not values:
        raise ValueError("List cannot be empty")

    return {
        "minimum": min(values),
        "maximum": max(values),
        "range": max(values) - min(values)
    }
''',

    "Text Analysis": '''import string

def analyze_text(text):
    cleaned = text.translate(
        str.maketrans("", "", string.punctuation)
    ).lower()

    words = cleaned.split()

    return {
        "total_words": len(words),
        "unique_words": len(set(words))
    }
'''
}

# Create output folder
output_dir = Path("generated_technical_content")
output_dir.mkdir(exist_ok=True)

print("----- TECHNICAL CONTENT AND PYTHON PROGRAM GENERATION -----")

# Generate content for each task
for _, row in df.iterrows():

    topic = row["Topic"]
    code = templates[topic]

    explanation = (
        f"Topic: {topic}\n"
        f"Audience: {row['Audience']}\n"
        f"Task: {row['Task_Description']}\n"
        f"Requirements: {row['Requirements']}\n"
        "Approach: validate inputs, process data and present a clear result."
    )

    file_stem = row["Task_ID"].lower()

    # Save Python program
    (output_dir / f"{file_stem}.py").write_text(
        code, encoding="utf-8"
    )

    # Save explanation
    (output_dir / f"{file_stem}_notes.txt").write_text(
        explanation, encoding="utf-8"
    )

    print(f"\nTask ID: {row['Task_ID']} | Topic: {topic}")
    print(explanation)

    print(
        "Saved:",
        f"{file_stem}.py",
        "and",
        f"{file_stem}_notes.txt"
    )

print("\nTotal generated files:", len(list(output_dir.iterdir())))

print("Template-based generation completed. No external LLM is called.")
