# Retail Sales Data Pipeline  
**End-to-End ETL Project (Python + SQLite + DuckDB + Parquet + Matplotlib)**  
Cleaned, validated, stored, and analyzed retail sales data with SQL queries and visual dashboards.

---

## Project Overview  
This project demonstrates a **complete data-engineering workflow** — from raw CSV extraction to data validation, transformation, storage, and visualization.  
It simulates a **mini data pipeline** that can later be scaled to cloud or production systems.

It covers:  
✅ Data cleaning & transformation  
✅ Validation checks on key columns  
✅ Loading into SQLite database  
✅ Generating reports & charts  
✅ Querying Parquet data using DuckDB (for analytics at scale)

---

## 🧩 Tech Stack  

| Layer | Tools Used |
|--------|-------------|
| Programming | Python (Pandas, NumPy) |
| Storage | SQLite, Parquet |
| Query Engine | DuckDB |
| Visualization | Matplotlib |
| ETL Process | Custom Python Scripts |
| Version Control | Git + GitHub |

---

## 🧠 Workflow Summary  

1. **Extract** → Read raw CSV from `/data/retail_sales.csv`  
2. **Transform** → Clean columns, handle missing values, compute monthly/yearly metrics  
3. **Validate** → Apply data-quality rules (e.g., unique transaction_id, non-negative revenue)  
4. **Load** → Store the clean data in SQLite (`retail_sales.db`)  
5. **Visualize** → Generate analytical charts (Top Categories, Monthly Revenue, Top Items)  
6. **Analyze** → Query Parquet data with DuckDB and export results as CSV  

---

## 🧾 Folder Structure  

retail_sales_data_pipeline/
│
├── data/
│ ├── retail_sales.csv
│ ├── cleaned_sales.csv
│ └── cleaned_sales.parquet
│
├── charts/
│ ├── revenue_by_category.png
│ ├── monthly_revenue_by_year.png
│ └── top_items_by_revenue.png
│
├── duckdb_outputs/
│ ├── top_categories.csv
│ └── monthly_revenue.csv
│
├── extract.py
├── clean_transform.py
├── validate.py
├── load_to_sqlite.py
├── make_charts.py
├── duckdb_queries.py
│
├── requirements.txt
├── .gitignore
└── README.md

---

---

## 🚀 How to Run

### 🧩 Step 1 — Setup Environment
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate      # (Windows: .venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

⚙️ Step 2 — Run ETL Pipeline

python extract.py
python clean_transform.py
python validate.py             # ✅ should print "Data validation passed"
python load_to_sqlite.py
python make_charts.py
python duckdb_queries.py



📊 3. Outputs
| Step         | Output                  | Location          |
| ------------ | ----------------------- | ----------------- |
| Cleaned Data | `cleaned_sales.csv`     | `/data`           |
| SQLite DB    | `retail_sales.db`       | root              |
| Charts       | `.png` files            | `/charts`         |
| Parquet File | `cleaned_sales.parquet` | `/data`           |
| SQL Reports  | `.csv` summaries        | `/duckdb_outputs` |


✅ Data-Validation Rules
| Rule                 | Description                                     |
| -------------------- | ----------------------------------------------- |
| Required Columns     | `transaction_id`, `transaction_date`, `revenue` |
| No Missing Values    | No nulls in critical columns                    |
| Non-Negative Revenue | All revenue ≥ 0                                 |
| Unique IDs           | Each `transaction_id` is unique                 |


📈 Example Visuals
| Chart                       | Description                                   |
| --------------------------- | --------------------------------------------- |
| **Revenue by Category**     | Top 10 categories contributing to total sales |
| **Monthly Revenue by Year** | Trend visualization across years              |
| **Top Items by Revenue**    | Highest-selling products overall              |


🧰 Skills Demonstrated

Python for Data Engineering
Pandas for Cleaning & Transformation
SQL + SQLite for Structured Data Storage
DuckDB for In-Memory Analytics
Parquet for Columnar Storage
Matplotlib for Visualization
Data Validation & Quality Checks
ETL Workflow Design
Git & GitHub for Version Control
