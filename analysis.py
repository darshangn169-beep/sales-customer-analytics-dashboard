import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
import os

# Download dataset
path = kagglehub.dataset_download("himanshuuike/superstore-sales-dataset")

print("Dataset downloaded at:", path)

# Find CSV file inside downloaded folder
files = os.listdir(path)
print("Files:", files)

# Assuming CSV file is inside
csv_file = [f for f in files if f.endswith('.csv')][0]

# Load dataset
df = pd.read_csv(os.path.join(path, csv_file))

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Total Sales & Profit
print("\nTotal Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(category_sales)

# Top Customers
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Customers:")
print(top_customers)

# Monthly Sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# 🔥 Profit Ratio
df['Profit Ratio'] = df['Profit'] / df['Sales']
print("\nAverage Profit Ratio:", df['Profit Ratio'].mean())

# 🔥 Loss making transactions
loss_products = df[df['Profit'] < 0]
print("\nNumber of loss-making transactions:", len(loss_products))

# 🔥 Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(region_sales)

region_sales.plot(kind='bar', title="Sales by Region")
plt.show()

# 🔥 Improved Monthly Trend
df.groupby(['Year','Month'])['Sales'].sum().plot(title="Sales Trend Over Time")
plt.show()

# Graphs
category_sales.plot(kind='bar', title="Sales by Category")
plt.show()

monthly_sales.plot(kind='line', title="Monthly Sales Trend")
plt.show()