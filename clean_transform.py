import os
import pandas as pd
import numpy as np

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_CSV = os.path.join(DATA_DIR, "retail_sales.csv")
CLEAN_CSV = os.path.join(DATA_DIR, "cleaned_sales.csv")

print("🔹 Reading:", RAW_CSV)
df = pd.read_csv(RAW_CSV)
print("Rows/cols BEFORE:", df.shape)

# --- Standardize column names (lowercase + underscores) ---
df.columns = (df.columns.str.strip()
                        .str.lower()
                        .str.replace(" ", "_")
                        .str.replace("-", "_"))

# now columns look like:
# transaction_id, customer_id, category, item, price_per_unit, quantity,
# total_spent, payment_method, location, transaction_date, discount_applied

# --- Dtypes ---
for c in ["price_per_unit", "quantity", "total_spent"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

if "transaction_date" in df.columns:
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

if "discount_applied" in df.columns:
    df["discount_applied"] = (
        df["discount_applied"].astype(str).str.strip().str.lower()
        .map({"true": True, "false": False, "yes": True, "no": False, "1": True, "0": False})
    )

# --- Remove dupes; drop rows missing critical fields ---
before = len(df)
df = df.drop_duplicates()
dupes_dropped = before - len(df)

critical = [c for c in ["transaction_id", "transaction_date", "total_spent"] if c in df.columns]
df = df.dropna(subset=critical)

# --- Fill non-critical text fields ---
for c in ["category", "item", "payment_method", "location"]:
    if c in df.columns:
        df[c] = df[c].fillna("Unknown")

# quantity: avoid NaN; keep as 0 if missing
if "quantity" in df.columns:
    df["quantity"] = df["quantity"].fillna(0)

# --- Add helpful columns ---
if "transaction_date" in df.columns:
    df["year"] = df["transaction_date"].dt.year
    df["month"] = df["transaction_date"].dt.month_name()

# sanity calc: average price per unit when quantity > 0
if all(c in df.columns for c in ["total_spent", "quantity"]):
    df["avg_price_calc"] = np.where(df["quantity"] > 0, df["total_spent"] / df["quantity"], np.nan)

# revenue alias
if "total_spent" in df.columns:
    df["revenue"] = df["total_spent"]

# --- Save cleaned CSV ---
os.makedirs(DATA_DIR, exist_ok=True)
df.to_csv(CLEAN_CSV, index=False)
print(f"✅ Cleaned file saved → {CLEAN_CSV} (rows: {len(df)}, duplicates removed: {dupes_dropped})")
print("Rows/cols AFTER:", df.shape)
print("\nSample rows after cleaning:\n", df.head(3))

# --- Simple summaries using your columns ---
if "category" in df.columns and "revenue" in df.columns:
    print("\n===== REVENUE by CATEGORY =====")
    print(df.groupby("category")["revenue"].sum().sort_values(ascending=False).head(10))

if "location" in df.columns and "revenue" in df.columns:
    print("\n===== REVENUE by LOCATION =====")
    print(df.groupby("location")["revenue"].sum().sort_values(ascending=False).head(10))

if "item" in df.columns and "revenue" in df.columns:
    print("\n===== TOP ITEMS by REVENUE =====")
    print(df.groupby("item")["revenue"].sum().sort_values(ascending=False).head(10))
