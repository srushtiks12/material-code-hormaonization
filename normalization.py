import csv
import re
import os


# -------------------------------
# Normalize description
# -------------------------------
def normalize_text(text):
    text = str(text).upper()

    # Standardize common terms
    text = re.sub(r"\bSS\b", "STAINLESS STEEL", text)
    text = re.sub(r"\bCS\b", "CARBON STEEL", text)
    text = re.sub(r"\bSCH\b", "SCHEDULE", text)
    text = re.sub(r"\bS40\b", "SCHEDULE 40", text)
    text = re.sub(r"\bS80\b", "SCHEDULE 80", text)

    # Convert quotation mark to INCH
    text = text.replace('"', ' INCH ')

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -------------------------------
# Convert size to millimetres
# -------------------------------
def convert_to_mm(size, unit):

    try:
        size = float(size)
    except ValueError:
        return None

    unit = str(unit).lower().strip()

    if unit in ["inch", "in", "inches"]:
        return size * 25.4

    elif unit in ["mm", "millimeter", "millimeters"]:
        return size

    else:
        return None


# -------------------------------
# Input files
# -------------------------------
files = [
    ("CPSE-A", "data/cpse_a.csv"),
    ("CPSE-B", "data/cpse_b.csv"),
    ("CPSE-C", "data/cpse_c.csv")
]


# Create output folder
os.makedirs("normalized_data", exist_ok=True)


# -------------------------------
# Process each CPSE
# -------------------------------
for cpse_name, input_file in files:

    output_file = f"normalized_data/{cpse_name.lower().replace('-', '_')}_normalized.csv"

    with open(input_file, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        rows = []

        for row in reader:

            normalized_description = normalize_text(
                row["description"]
            )

            size_mm = convert_to_mm(
                row["size"],
                row["unit"]
            )

            row["normalized_description"] = normalized_description
            row["standard_size_mm"] = size_mm

            rows.append(row)


    # Save normalized data
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


    print(f"{cpse_name} normalization completed.")
    print(f"Saved to: {output_file}")


print("\nNormalization completed successfully!")