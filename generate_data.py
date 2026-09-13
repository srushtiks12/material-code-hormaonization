import csv
import os

os.makedirs("data", exist_ok=True)


def create_csv(filename, cpse, materials):

    columns = [
        "material_code",
        "description",
        "size",
        "unit",
        "grade",
        "schedule",
        "cpse"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(columns)

        for material in materials:
            writer.writerow(material + [cpse])


# CPSE-A
cpse_a = [
    ["MAT1001", "SS PIPE 2 IN SCH 40", 2, "inch", "SS", "40"],
    ["MAT1002", "CARBON STEEL PIPE 3 IN SCH 80", 3, "inch", "CS", "80"],
    ["MAT1003", "SS ELBOW 2 IN 90 DEG", 2, "inch", "SS", "N/A"],
    ["MAT1004", "HEX BOLT M10 X 50 SS", 10, "mm", "SS", "N/A"],
    ["MAT1005", "CARBON STEEL FLANGE 4 IN", 4, "inch", "CS", "N/A"]
]


# CPSE-B
cpse_b = [
    ["458921", "STAINLESS STEEL PIPE 50.8 MM S40", 50.8, "mm", "SS", "40"],
    ["458922", "CS PIPE 3 INCH SCHEDULE 80", 3, "inch", "CS", "80"],
    ["458923", "SS 90 DEG ELBOW 50.8MM", 50.8, "mm", "SS", "N/A"],
    ["458924", "STAINLESS HEX BOLT M10X50", 10, "mm", "SS", "N/A"],
    ["458925", "CS FLANGE 4 IN", 4, "inch", "CS", "N/A"]
]


# CPSE-C
cpse_c = [
    ["CP7781", 'SS PIPE 2" SCHEDULE 40', 2, "inch", "SS", "40"],
    ["CP7782", "CARBON STEEL PIPE 76.2 MM SCH 80", 76.2, "mm", "CS", "80"],
    ["CP7783", "STAINLESS STEEL ELBOW 2 INCH 90 DEG", 2, "inch", "SS", "N/A"],
    ["CP7784", "SS HEXAGONAL BOLT M10 X 50 MM", 10, "mm", "SS", "N/A"],
    ["CP7785", "CARBON STEEL FLANGE 101.6 MM", 101.6, "mm", "CS", "N/A"]
]


create_csv("data/cpse_a.csv", "CPSE-A", cpse_a)
create_csv("data/cpse_b.csv", "CPSE-B", cpse_b)
create_csv("data/cpse_c.csv", "CPSE-C", cpse_c)


print("========================================")
print("CPSE datasets created successfully!")
print("========================================")

print("\nCreated files:")
print("1. data/cpse_a.csv")
print("2. data/cpse_b.csv")
print("3. data/cpse_c.csv")

print("\nEach CPSE contains 5 materials.")