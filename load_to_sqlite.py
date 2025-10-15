import os
import pandas as pd
from sqlalchemy import create_engine

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLEAN_CSV = os.path.join(DATA_DIR, "cleaned_sales.csv")
DB_PATH = os.path.join(BASE_DIR, "retail_sales.db")

print("🔹 Reading cleaned CSV:", CLEAN_CSV)
df = pd.read_csv(CLEAN_CSV)

# --- Create SQLite database ---
engine = create_engine(f"sqlite:///{DB_PATH}")

print("🔹 Writing to SQLite table 'sales_data' ...")
df.to_sql("sales_data", con=engine, index=False, if_exists="replace")
print(f"✅ Wrote {len(df)} rows to {DB_PATH}")

# --- SQL Queries for quick validation ---
print("\n===== TOP CATEGORY by REVENUE (SQL) =====")
q1 = """
SELECT category, SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 5;
"""
print(pd.read_sql(q1, con=engine))

print("\n===== MONTHLY REVENUE (SQL) =====")
q2 = """
SELECT year, month, SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY year, month
ORDER BY year,
       CASE month
         WHEN 'January' THEN 1 WHEN 'February' THEN 2 WHEN 'March' THEN 3
         WHEN 'April' THEN 4 WHEN 'May' THEN 5 WHEN 'June' THEN 6
         WHEN 'July' THEN 7 WHEN 'August' THEN 8 WHEN 'September' THEN 9
         WHEN 'October' THEN 10 WHEN 'November' THEN 11 WHEN 'December' THEN 12
       END;
"""
print(pd.read_sql(q2, con=engine))

print("\n✅ Done! Database created →", DB_PATH)
