# Retail Sales Data Pipeline (Python + SQLite + DuckDB)

End-to-end project: **Extract → Transform → Validate → Load → Analyze → Visualize**

**Tech Stack:** Python · Pandas · SQLite · Matplotlib · DuckDB · Parquet  
**Dataset:** ~12,000 retail transactions → ~11,971 after cleaning

---

## 🗂 Project Structure
retail_sales_data_pipeline/
├─ data/ # raw & cleaned data (CSV/Parquet)
├─ duckdb_outputs/ # SQL outputs from DuckDB
├─ charts/ # generated charts
├─ extract.py # read raw CSV, preview data
├─ clean_transform.py # clean + transform → cleaned_sales.csv
├─ validate.py # data validation (columns, duplicates, etc.)
├─ load_to_sqlite.py # save cleaned data to retail_sales.db
├─ make_charts.py # visualize key insights
├─ duckdb_queries.py # run SQL on Parquet + export results
└─ requirements.txt


---

## 🚀 How to Run

### 1️⃣ Setup Environment
```bash
python -m venv .venv
source .venv/bin/activate        # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
2️⃣ Extract → Transform → Validate

python extract.py
python clean_transform.py
python validate.py                 # ✅ should print “Data validation passed”
3️⃣ Load to SQLite
python load_to_sqlite.py

4️⃣ Generate Charts
python make_charts.py

5️⃣ Run DuckDB SQL Queries
python duckdb_queries.py


📊 Outputs
Cleaned data → data/cleaned_sales.csv
Parquet file → data/cleaned_sales.parquet
SQLite database → retail_sales.db (table sales_data)
Charts → charts/*.png
SQL summaries → duckdb_outputs/*.csv

✅ Data Validation Rules
Required columns present: transaction_id, transaction_date, revenue
No null transaction dates
No negative revenue
Unique transaction_id


💡 Skills Demonstrated
Python | Pandas | SQL | SQLite | DuckDB | Data Cleaning | ETL | Parquet | Matplotlib | Data Visualization