import os, duckdb

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, "data", "cleaned_sales.csv")
PARQUET = os.path.join(BASE, "data", "cleaned_sales.parquet")
OUT_DIR = os.path.join(BASE, "duckdb_outputs")
os.makedirs(OUT_DIR, exist_ok=True)

con = duckdb.connect()

# OPTIONAL: write Parquet using DuckDB (no pyarrow needed)
con.execute(f"""
  COPY (
    SELECT * FROM read_csv_auto('{CSV}')
  )
  TO '{PARQUET}' (FORMAT 'parquet');
""")
print("✅ Saved Parquet via DuckDB:", PARQUET)

# 1) Top categories by revenue (querying the CSV directly)
cat = con.execute(f"""
  SELECT category, SUM(revenue) AS total_revenue
  FROM read_csv_auto('{CSV}')
  GROUP BY category
  ORDER BY total_revenue DESC
  LIMIT 10;
""").df()
cat.to_csv(os.path.join(OUT_DIR, "top_categories.csv"), index=False)

# 2) Monthly revenue by year
monthly = con.execute(f"""
  SELECT year, month, SUM(revenue) AS total_revenue
  FROM read_csv_auto('{CSV}')
  GROUP BY year, month
  ORDER BY year,
    CASE month
      WHEN 'January' THEN 1 WHEN 'February' THEN 2 WHEN 'March' THEN 3
      WHEN 'April' THEN 4 WHEN 'May' THEN 5 WHEN 'June' THEN 6
      WHEN 'July' THEN 7 WHEN 'August' THEN 8 WHEN 'September' THEN 9
      WHEN 'October' THEN 10 WHEN 'November' THEN 11 WHEN 'December' THEN 12
    END;
""").df()
monthly.to_csv(os.path.join(OUT_DIR, "monthly_revenue.csv"), index=False)

print("✅ Wrote:", os.path.join(OUT_DIR, "top_categories.csv"))
print("✅ Wrote:", os.path.join(OUT_DIR, "monthly_revenue.csv"))
