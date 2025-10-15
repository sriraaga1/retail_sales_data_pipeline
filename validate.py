import pandas as pd
import sys, os

CLEAN = os.path.join("data", "cleaned_sales.csv")
df = pd.read_csv(CLEAN)

issues = []

# 1) must have rows
if len(df) == 0:
    issues.append("dataset is empty")

# 2) required columns exist
required = ["transaction_id","transaction_date","revenue"]
missing = [c for c in required if c not in df.columns]
if missing:
    issues.append(f"missing columns: {missing}")

# 3) no nulls in critical columns
if df["transaction_date"].isna().any():
    issues.append("transaction_date has nulls")

# 4) revenue should be non-negative
if (df["revenue"] < 0).any():
    issues.append("negative revenue found")

# 5) transaction_id should be unique
if not df["transaction_id"].is_unique:
    issues.append("duplicate transaction_id values found")

if issues:
    print("❌ Data validation failed:")
    for i in issues: print(" -", i)
    sys.exit(1)
else:
    print("✅ Data validation passed. Rows:", len(df))
