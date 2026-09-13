import pandas as pd


# Load matching results
matches = pd.read_csv("material_matches.csv")


# Store groups of matched materials
groups = []

# Track which material codes are already assigned
assigned_codes = set()


# Generate NMC codes
nmc_number = 1


for _, row in matches.iterrows():

    code1 = row["Code 1"]
    code2 = row["Code 2"]

    # Check whether either material is already grouped
    existing_group = None

    for group in groups:

        if code1 in group["codes"] or code2 in group["codes"]:
            existing_group = group
            break

    # If group already exists
    if existing_group:

        existing_group["codes"].add(code1)
        existing_group["codes"].add(code2)

        existing_group["confidence"].append(
            row["Final Score"]
        )

    # Otherwise create a new group
    else:

        group = {
            "nmc": f"NMC-{nmc_number:04d}",
            "codes": {code1, code2},
            "confidence": [row["Final Score"]]
        }

        groups.append(group)

        nmc_number += 1


# --------------------------------------------------
# CREATE FINAL OUTPUT
# --------------------------------------------------

final_rows = []


for group in groups:

    nmc = group["nmc"]

    average_confidence = round(
        sum(group["confidence"]) / len(group["confidence"]),
        2
    )

    for code in group["codes"]:

        # Find material information from matching data
        material = None

        for _, row in matches.iterrows():

            if row["Code 1"] == code:
                material = {
                    "CPSE": row["CPSE 1"],
                    "Description": row["Description 1"]
                }
                break

            if row["Code 2"] == code:
                material = {
                    "CPSE": row["CPSE 2"],
                    "Description": row["Description 2"]
                }
                break

        if material:

            final_rows.append({
                "CPSE": material["CPSE"],
                "Legacy Code": code,
                "Description": material["Description"],
                "Common NMC": nmc,
                "Confidence": average_confidence
            })


# Convert to DataFrame
final_df = pd.DataFrame(final_rows)


# Save final result
final_df.to_csv(
    "final_nmc_mapping.csv",
    index=False
)


# Display
print("\n==============================================")
print(" FINAL NMC MATERIAL HARMONIZATION")
print("==============================================\n")

print(final_df.to_string(index=False))

print("\n==============================================")
print("Final file created:")
print("final_nmc_mapping.csv")
print("==============================================")