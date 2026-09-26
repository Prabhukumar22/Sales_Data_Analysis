import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]

print("\n--- SALES DATA ---")
print(df)

print("\n--- DATA INFORMATION ---")
print(df.info())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\n--- REVENUE BY PRODUCT ---")
print(product_sales)

region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("\n--- REVENUE BY REGION ---")
print(region_sales)

df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\n--- MONTHLY REVENUE ---")
print(monthly_sales)

top_product = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\n--- PRODUCT QUANTITY ---")
print(top_product)

product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

print("\n--- KEY INSIGHTS ---")
print("1. Revenue varies significantly across products and regions.")
print("2. Electronics products contribute substantial revenue because of higher unit prices.")
print("3. Accessories generate higher sales volumes because of their lower prices.")
print("4. Regional revenue can be compared to identify stronger markets.")
