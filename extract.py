import os
import pandas as pd

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(DATA_DIR, "retail_sales.csv")

print("🔹 Reading CSV from:", CSV_PATH)
df = pd.read_csv(CSV_PATH)

# --- Quick look at data ---
print("\n===== HEAD (first 5 rows) =====")
print(df.head())

print("\n===== INFO (data types & non-null counts) =====")
print(df.info())

print("\n===== NULL VALUES BY COLUMN =====")
print(df.isna().sum())

# --- Simple summaries ---
if "Region" in df.columns:
    print("\n===== TOTAL SALES BY REGION =====")
    print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

if "Category" in df.columns:
    print("\n===== TOTAL SALES BY CATEGORY =====")
    print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
