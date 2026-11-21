
# Experiment 13: AI-Powered Study Assistant

import pandas as pd
import re

# Read study materials CSV file
df = pd.read_csv("experiment_13_study_materials.csv")


# Function to extract searchable words
def tokenize(text):
    return set(re.findall(r"[a-zA-Z]+", str(text).lower()))


# Function to retrieve relevant study material
def retrieve_material(query):

    query_words = tokenize(query)
    scores = []

    for _, row in df.iterrows():

        searchable_text = " ".join([
            row["Topic"],
            row["Concept"],
            row["Explanation"],
            row["Keywords"]
        ])

        material_words = tokenize(searchable_text)

        score = len(query_words & material_words) / max(len(query_words), 1)

        scores.append(score)

    best_index = scores.index(max(scores))

    if scores[best_index] == 0:
        return None, 0

    return df.iloc[best_index], scores[best_index]


# Function to display study notes and quiz
def study_assistant(query):

    material, score = retrieve_material(query)

    if material is None:
        print("No matching material found. Try another concept.")
        return

    print("\n----- PERSONALIZED STUDY NOTES -----")

    print("Topic       :", material["Topic"])
    print("Concept     :", material["Concept"])
    print("Explanation :", material["Explanation"])
    print("Match score :", round(score * 100, 2), "%")

    print("\n----- QUICK QUIZ -----")

    print("Question    :", material["Quiz_Question"])
    print("Difficulty  :", material["Difficulty"])
    print("Answer      :", material["Answer"])


# Display available concepts
print("Available concepts:",
      ", ".join(df["Concept"].tolist()))

# Get user input
query = input("\nEnter a topic or concept to study: ")

# Run study assistant
study_assistant(query)

print("\nStudy assistant session completed.")

print("Note: Matching is based on CSV keyword overlap, not a live Generative AI model.")
