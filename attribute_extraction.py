import csv
import re
import os


# --------------------------------
# Extract material type
# --------------------------------
def extract_material(description):

    if "STAINLESS STEEL" in description:
        return "STAINLESS STEEL"

    elif "CARBON STEEL" in description:
        return "CARBON STEEL"

    else:
        return "UNKNOWN"


# --------------------------------
# Extract component
# --------------------------------
def extract_component(description):

    components = [
        "PIPE",
        "ELBOW",
        "BOLT",
        "FLANGE"
    ]

    for component in components:

        if re.search(r"\b" + component + r"\b", description):
            return component

    return "UNKNOWN"


# --------------------------------
# Extract schedule
# --------------------------------
def extract_schedule(description):

    match = re.search(
        r"SCHEDULE\s*(\d+)",
        description
    )

    if match:
        return match.group(1)

    return "N/A"


# --------------------------------
# Input normalized files
# --------------------------------
files = [
    ("CPSE-A", "normalized_data/cpse_a_normalized.csv"),
    ("CPSE-B", "normalized_data/cpse_b_normalized.csv"),
    ("CPSE-C", "normalized_data/cpse_c_normalized.csv")
]


# --------------------------------
# Create output folder
# --------------------------------
os.makedirs("structured_data", exist_ok=True)


# --------------------------------
# Process each CPSE
# --------------------------------
for cpse_name, input_file in files:

    output_file = (
        f"structured_data/"
        f"{cpse_name.lower().replace('-', '_')}_structured.csv"
    )

    rows = []

    with open(
        input_file,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            description = row["normalized_description"]

            # Extract technical attributes
            material = extract_material(description)

            component = extract_component(description)

            schedule = extract_schedule(description)

            # Add extracted attributes
            row["material_type"] = material
            row["component"] = component
            row["extracted_schedule"] = schedule

            rows.append(row)


    # --------------------------------
    # Save structured data
    # --------------------------------
    fieldnames = list(rows[0].keys())

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)


    print(f"{cpse_name} attribute extraction completed.")
    print(f"Saved to: {output_file}")


print("\nTechnical attribute extraction completed successfully!")