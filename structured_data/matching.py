import csv
from rapidfuzz import fuzz


# ---------------------------------------
# Read structured CSV file
# ---------------------------------------
def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


# ---------------------------------------
# Calculate matching score
# ---------------------------------------
def calculate_match(material1, material2):

    score = 0
    reasons = []

    # Material type comparison
    if material1["material_type"] == material2["material_type"]:
        score += 25
        reasons.append("Material type matches")

    # Component comparison
    if material1["component"] == material2["component"]:
        score += 20
        reasons.append("Component matches")

    # Size comparison
    try:
        size1 = float(material1["standard_size_mm"])
        size2 = float(material2["standard_size_mm"])

        if abs(size1 - size2) < 0.1:
            score += 25
            reasons.append("Size matches")
    except (ValueError, TypeError):
        pass

    # Schedule comparison
    if material1["extracted_schedule"] == material2["extracted_schedule"]:
        score += 15
        reasons.append("Schedule matches")

    # Description similarity
    similarity = fuzz.token_set_ratio(
        material1["normalized_description"],
        material2["normalized_description"]
    )

    # Give up to 15 points for description similarity
    description_score = similarity * 0.15
    score += description_score

    if similarity >= 80:
        reasons.append("Description is highly similar")

    return round(score, 2), round(similarity, 2), reasons


# ---------------------------------------
# Load CPSE data
# ---------------------------------------
cpse_a = read_csv(
    "structured_data/cpse_a_structured.csv"
)

cpse_b = read_csv(
    "structured_data/cpse_b_structured.csv"
)

cpse_c = read_csv(
    "structured_data/cpse_c_structured.csv"
)


# ---------------------------------------
# Compare materials
# ---------------------------------------
all_data = [
    ("CPSE-A", cpse_a),
    ("CPSE-B", cpse_b),
    ("CPSE-C", cpse_c)
]


print("=" * 70)
print("           CPSE MATERIAL MATCHING")
print("=" * 70)


# Compare every pair of CPSEs
for i in range(len(all_data)):

    cpse1_name, data1 = all_data[i]

    for j in range(i + 1, len(all_data)):

        cpse2_name, data2 = all_data[j]

        print("\n" + "-" * 70)
        print(f"{cpse1_name}  vs  {cpse2_name}")
        print("-" * 70)

        for material1 in data1:

            for material2 in data2:

                score, similarity, reasons = calculate_match(
                    material1,
                    material2
                )

                # Only show promising matches
                if score >= 70:

                    print("\nPOTENTIAL MATCH")

                    print(
                        f"{cpse1_name}: "
                        f"{material1['material_code']}"
                    )

                    print(
                        f"Description: "
                        f"{material1['normalized_description']}"
                    )

                    print(
                        f"{cpse2_name}: "
                        f"{material2['material_code']}"
                    )

                    print(
                        f"Description: "
                        f"{material2['normalized_description']}"
                    )

                    print(f"\nMatching Score: {score}%")
                    print(
                        f"Description Similarity: "
                        f"{similarity}%"
                    )

                    print("\nWhy did the system match them?")

                    for reason in reasons:
                        print("✓", reason)


print("\n" + "=" * 70)
print("Matching completed!")
print("=" * 70)