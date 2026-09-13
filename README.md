# 🤖 AI-Driven Standardization and Harmonization of Material Codes Across CPSEs

## 📌 Overview

Different Central Public Sector Enterprises (CPSEs) may use different material codes and descriptions for the same or similar materials. This can make it difficult to identify equivalent materials, avoid duplicates, and maintain consistent material records across organizations.

This project presents an **AI-assisted material harmonization system** that processes material data from different CPSEs, standardizes their descriptions, identifies equivalent materials, and generates a common **National Material Code (NMC)** while preserving the original CPSE material codes.

## 🎯 Objectives

* Standardize material descriptions from different CPSEs.
* Extract important technical attributes from material descriptions.
* Identify equivalent or similar materials.
* Apply AI-based semantic similarity for intelligent matching.
* Generate a common National Material Code (NMC).
* Preserve existing CPSE/legacy material codes.

## 🔄 System Workflow

```text
CPSE Material Data
        ↓
Data Preprocessing
        ↓
Text Normalization
        ↓
Technical Attribute Extraction
        ↓
AI Semantic Similarity
        ↓
Fuzzy Matching + Attribute Comparison
        ↓
Material Match Results
        ↓
Common NMC Generation
```

## 🧠 AI-Based Approach

The system combines multiple techniques to improve material matching.

### Text Normalization

Material descriptions are standardized by expanding abbreviations, standardizing terminology, units, sizes, and other commonly varying formats.

### Technical Attribute Extraction

Important information such as **material type, component, size, grade, and schedule** is extracted from the material descriptions.

### Semantic Matching

The project uses **Sentence Transformers (`all-MiniLM-L6-v2`)** to calculate semantic similarity between normalized material descriptions. This helps identify materials with different wording but similar meaning.

### Fuzzy Matching

**RapidFuzz** is used to calculate textual similarity and support the matching process.

### Attribute Comparison

Technical attributes are compared along with semantic and textual similarity to improve the reliability of matching.

## 🏷️ Common National Material Code (NMC)

After identifying equivalent materials, the system assigns a common NMC while retaining the original CPSE codes.

**Example:**

| CPSE   | Original Code | Description                      | Common NMC |
| ------ | ------------- | -------------------------------- | ---------- |
| CPSE-A | MAT1001       | SS PIPE 2 IN SCH 40              | NMC-0001   |
| CPSE-B | 458921        | STAINLESS STEEL PIPE 50.8 MM S40 | NMC-0001   |
| CPSE-C | CP7781        | SS PIPE 2" SCH 40                | NMC-0001   |

This allows existing material records to be preserved while providing a standardized reference.

## 🛠️ Technology Stack

* **Python**
* **Pandas** – Data processing
* **Sentence Transformers** – Semantic similarity
* **RapidFuzz** – Fuzzy matching
* **Scikit-learn** – Supporting ML utilities
* **CSV** – Dataset and output storage

## 📂 Project Structure

```text
sih/
├── data/
├── normalized_data/
├── structured_data/
├── attribute_extraction.py
├── normalization.py
├── semantic_matching.py
├── nmc_generator.py
├── generate_data.py
├── main.py
├── material_matches.csv
├── final_nmc_mapping.csv
└── requirements.txt
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/srushtiks12/material-code-hormaonization.git
cd sih
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

Execute the Python modules according to the workflow:

```text
Data → Normalization → Attribute Extraction
→ Semantic Matching → NMC Generation
```

The system generates matching and harmonized material mapping results.

## 📊 Output

The project generates structured output files including:

* `material_matches.csv` – Material similarity and matching results.
* `final_nmc_mapping.csv` – Final mapping of CPSE material codes to common NMCs.

## 💡 Key Innovation

The proposed approach combines **AI-based semantic similarity, fuzzy matching, and technical attribute comparison** to identify equivalent materials even when different CPSEs use different descriptions, abbreviations, or formats.

## 🏆 Smart India Hackathon 2026

**Problem Statement ID:** SIH26099
**Problem Statement:** AI-Driven Standardization and Harmonization of Material Codes Across CPSEs

This project was developed as a prototype for **Smart India Hackathon 2026**, demonstrating how AI and natural language processing can support material standardization and interoperability across CPSEs.

## ⚠️ Prototype Scope

This repository demonstrates the core workflow using sample/structured material datasets. Further validation, larger real-world datasets, security, and enterprise integration would be required for production deployment.
