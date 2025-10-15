import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHARTS_DIR = os.path.join(BASE_DIR, "charts")
CLEAN_CSV = os.path.join(DATA_DIR, "cleaned_sales.csv")

os.makedirs(CHARTS_DIR, exist_ok=True)

df = pd.read_csv(CLEAN_CSV)

# 1) Revenue by Category (Top 10)
cat = (df.groupby("category")["revenue"].sum()
         .sort_values(ascending=False).head(10))
ax1 = cat.plot(kind="bar", title="Revenue by Category (Top 10)")
ax1.set_xlabel("Category"); ax1.set_ylabel("Revenue")
fig1 = ax1.get_figure(); fig1.tight_layout()
p1 = os.path.join(CHARTS_DIR, "revenue_by_category.png")
fig1.savefig(p1); plt.close(fig1)
print("✅ Saved:", p1)

# 2) Monthly Revenue by Year
month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]
if "month" in df.columns:
    df["month"] = pd.Categorical(df["month"], month_order, ordered=True)

month = (df.groupby(["year","month"])["revenue"].sum()
          .reset_index().sort_values(["year","month"]))
pivot = month.pivot(index="month", columns="year", values="revenue")
ax2 = pivot.plot(kind="bar", title="Monthly Revenue by Year")
ax2.set_xlabel("Month"); ax2.set_ylabel("Revenue")
fig2 = ax2.get_figure(); fig2.tight_layout()
p2 = os.path.join(CHARTS_DIR, "monthly_revenue_by_year.png")
fig2.savefig(p2); plt.close(fig2)
print("✅ Saved:", p2)

print("Charts ready in the 'charts/' folder.")
# --- 3) Top 10 Items by Revenue ---
print("\n=== Generating Top 10 Items by Revenue Chart ===")

top_items = (df.groupby("item")["revenue"].sum()
               .sort_values(ascending=False).head(10))

ax3 = top_items.plot(kind="bar", title="Top 10 Items by Revenue")
ax3.set_xlabel("Item")
ax3.set_ylabel("Revenue")

fig3 = ax3.get_figure()
fig3.tight_layout()

p3 = os.path.join(CHARTS_DIR, "top_items_by_revenue.png")
fig3.savefig(p3)
plt.close(fig3)

print("✅ Saved:", p3)
