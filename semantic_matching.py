import pandas as pd
from rapidfuzz import fuzz
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load AI semantic model
print("Loading AI model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("AI model loaded successfully!\n")


# --------------------------------------------------
# AI SEMANTIC SIMILARITY
# --------------------------------------------------

def semantic_similarity(description1, description2):

    embedding1 = model.encode([description1])
    embedding2 = model.encode([description2])

    score = cosine_similarity(embedding1, embedding2)[0][0]

    return float(score) * 100


# --------------------------------------------------
# MATERIAL MATCHING
# --------------------------------------------------

def calculate_match(row1, row2):

    score = 0
    reasons = []

    # Material type
    if row1["material_type"] == row2["material_type"]:
        score += 20
        reasons.append("Same material type")

    # Component
    if row1["component"] == row2["component"]:
        score += 20
        reasons.append("Same component")

    # Size
    if abs(
        float(row1["standard_size_mm"])
        - float(row2["standard_size_mm"])
    ) <= 0.1:

        score += 20
        reasons.append("Same size")

    # Schedule
    if str(row1["extracted_schedule"]) == str(row2["extracted_schedule"]):
        score += 15
        reasons.append("Same schedule")

    # Fuzzy description similarity
    fuzzy_score = fuzz.token_set_ratio(
        str(row1["normalized_description"]),
        str(row2["normalized_description"])
    )

    fuzzy_points = (fuzzy_score / 100) * 10
    score += fuzzy_points

    # AI semantic similarity
    ai_score = semantic_similarity(
        str(row1["normalized_description"]),
        str(row2["normalized_description"])
    )

    ai_points = (ai_score / 100) * 15
    score += ai_points

    if ai_score >= 80:
        reasons.append("High AI semantic similarity")

    return round(score, 2), round(ai_score, 2), reasons


# --------------------------------------------------
# LOAD STRUCTURED DATA
# --------------------------------------------------

files = {
    "CPSE-A": "structured_data/cpse_a_structured.csv",
    "CPSE-B": "structured_data/cpse_b_structured.csv",
    "CPSE-C": "structured_data/cpse_c_structured.csv"
}

data = {}

for cpse, file in files.items():

    print("Loading:", file)

    data[cpse] = pd.read_csv(file)


# --------------------------------------------------
# COMPARE MATERIALS
# --------------------------------------------------

print("\n==============================================")
print(" AI-DRIVEN MATERIAL HARMONIZATION")
print("==============================================\n")

matches = []


for cpse1 in data:

    for cpse2 in data:

        # Don't compare CPSE-A with itself
        if cpse1 >= cpse2:
            continue

        df1 = data[cpse1]
        df2 = data[cpse2]

        for _, row1 in df1.iterrows():

            for _, row2 in df2.iterrows():

                final_score, ai_score, reasons = calculate_match(
                    row1,
                    row2
                )

                # Consider scores >= 70 as potential matches
                if final_score >= 70:

                    matches.append({

                        "CPSE 1": cpse1,
                        "Code 1": row1["material_code"],
                        "Description 1": row1["description"],

                        "CPSE 2": cpse2,
                        "Code 2": row2["material_code"],
                        "Description 2": row2["description"],

                        "AI Similarity": ai_score,
                        "Final Score": final_score,

                        "Reasons": ", ".join(reasons)
                    })


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if matches:

    result_df = pd.DataFrame(matches)

    print("\nMATCHED MATERIALS:\n")

    print(result_df.to_string(index=False))

    # Save results
    result_df.to_csv(
        "material_matches.csv",
        index=False
    )

    print("\n==============================================")
    print("Results saved successfully!")
    print("File: material_matches.csv")
    print("==============================================")

else:

    print("No matching materials found.")