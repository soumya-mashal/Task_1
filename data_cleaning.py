import pandas as pd
import numpy as np

df = pd.read_csv('assessments.csv')

print("--- Missing Values ---")
print("Missing values before handling:")
print(df.isnull().sum())


df['date'] = df['date'].replace('', np.nan)


df['date'] = pd.to_numeric(df['date'], errors='coerce')

print("\nMissing values after initial handling:")
print(df.isnull().sum())


print("\n--- Duplicate Rows ---")
print("Number of duplicate rows before removal:", df.duplicated().sum())


df_cleaned = df.drop_duplicates()

print("Number of duplicate rows after removal:", df_cleaned.duplicated().sum())
print("Shape of DataFrame after removing duplicates:", df_cleaned.shape)

# --- Step 3: Standardize Text Values 

print("\n--- Text Standardization ---")
for col in ['code_module', 'code_presentation', 'assessment_type']:
    if col in df_cleaned.columns:
        df_cleaned[col] = df_cleaned[col].str.strip()
        print(f"Standardized column: {col}")

# --- Step 4: Convert Date Formats ---


print("\n--- Date Format Check ---")
print("Data type of 'date' column:", df_cleaned['date'].dtype)

#  Step 5: Rename Column Headers 
print("\n--- Rename Column Headers ---")
df_cleaned.rename(columns={'code_module': 'code_module',
                           'code_presentation': 'code_presentation',
                           'id_assessment': 'id_assessment',
                           'assessment_type': 'assessment_type',
                           'date': 'date',
                           'weight': 'weight'}, inplace=True)
print("Column headers after renaming (already were clean):", df_cleaned.columns.tolist())

# --- Step 6: Check and Fix Data Types ---
print("\n--- Data Type Check ---")
print("Data types before conversion:")
print(df_cleaned.dtypes)


df_cleaned['weight'] = pd.to_numeric(df_cleaned['weight'], errors='coerce')

print("\nData types after conversion:")
print(df_cleaned.dtypes)

# --- Step 7: Save the Cleaned Dataset ---
df_cleaned.to_csv('cleaned_assessments.csv', index=False)
print("\nCleaned dataset saved as cleaned_assessments.csv")

# --- Short Summary of Changes ---
summary = """
Data Cleaning Summary for assessments.csv:

1.  **Missing Values:**
    - Identified missing values in the 'date' column (represented by empty strings).
    - Replaced empty strings in the 'date' column with NaN.
    - Converted the 'date' column to a numeric type (float64), with non-numeric values becoming NaN.
    - The remaining NaN values in 'date' likely correspond to Exam dates where the 'date' was not provided.

2.  **Duplicate Rows:**
    - Checked for duplicate rows and removed them. The shape of the DataFrame was inspected before and after.

3.  **Text Standardization:**
    - Applied `.strip()` to the 'code_module', 'code_presentation', and 'assessment_type' columns to remove any leading or trailing whitespace.

4.  **Date Format Conversion:**
    - The 'date' column was already in a numeric format (days). Missing values were handled. No further format conversion was needed.

5.  **Column Renaming:**
    - The column headers were already clean and uniform, so no renaming was strictly necessary, but the code for renaming is included for completeness.

6.  **Data Type Checking:**
    - Checked the data types of all columns.
    - Ensured the 'weight' column is of a numeric type (float64).

The cleaned dataset is saved as 'cleaned_assessments.csv'.
"""

print("\n--- Summary of Changes ---")
print(summary)

# You would also save this summary to your README.md file on GitHub
with open('README.md', 'w') as f:
    f.write("# Data Cleaning Task 1 - Assessments Dataset\n\n")
    f.write(summary)
print("\nSummary saved to README.md")
