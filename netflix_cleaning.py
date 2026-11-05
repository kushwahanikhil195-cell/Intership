import pandas as pd

# Load dataset
df = pd.read_csv(
    r"C:\Users\Nikhil kusahwa\Downloads\archive (4)\netflix_titles.csv"
)

# Display dataset information
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna("Unknown")

# Remove extra spaces
for col in df.columns:
    df[col] = df[col].map(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# Standardize date format
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)

df["date_added"] = df["date_added"].dt.strftime("%Y-%m-%d")
df["date_added"] = df["date_added"].fillna("Unknown")

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Final dataset shape
print("\nFinal Dataset Shape:")
print(df.shape)

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")