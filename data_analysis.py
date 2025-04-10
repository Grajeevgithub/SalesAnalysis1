
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
# Make sure the file 'sales_data.csv' is in the same directory as this script
data = pd.read_csv('sales_data.csv')

# Step 2: Display the first few rows and dataset info
print("First few rows of the dataset:")
print(data.head())
print("\nDataset Info:")
print(data.info())

# Step 3: Data Cleaning
# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Drop rows with missing values
data = data.dropna()

# Remove duplicate rows
data = data.drop_duplicates()

# Confirm no missing values or duplicates remain
print("\nAfter cleaning, missing values and duplicates:")
print("Missing values:\n", data.isnull().sum())
print("Duplicate rows:", data.duplicated().sum())

# Step 4: Basic Data Analysis
# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Group sales by region
print("\nSales by Region:")
sales_by_region = data.groupby('Region')['Sales'].sum()
print(sales_by_region)

# Step 5: Data Visualization
# 1. Bar plot of sales by region
plt.figure(figsize=(10, 6))
sales_by_region.plot(kind='bar', color='skyblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

# 2. Sales trend over time (if 'Date' column exists)
if 'Date' in data.columns:
    # Ensure 'Date' is a datetime column
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Group sales by date
    sales_trend = data.groupby('Date')['Sales'].sum()
    
    plt.figure(figsize=(10, 6))
    sales_trend.plot(color='green')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.show()
else:
    print("\nThe dataset does not have a 'Date' column.")

# 3. Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
# Make sure the file 'sales_data.csv' is in the same directory as this script
data = pd.read_csv('sales_data.csv')

# Step 2: Display the first few rows and dataset info
print("First few rows of the dataset:")
print(data.head())
print("\nDataset Info:")
print(data.info())

# Step 3: Data Cleaning
# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Drop rows with missing values
data = data.dropna()

# Remove duplicate rows
data = data.drop_duplicates()

# Confirm no missing values or duplicates remain
print("\nAfter cleaning, missing values and duplicates:")
print("Missing values:\n", data.isnull().sum())
print("Duplicate rows:", data.duplicated().sum())

# Step 4: Basic Data Analysis
# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Group sales by region
print("\nSales by Region:")
sales_by_region = data.groupby('Region')['Sales'].sum()
print(sales_by_region)

# Step 5: Data Visualization
# 1. Bar plot of sales by region
plt.figure(figsize=(10, 6))
sales_by_region.plot(kind='bar', color='skyblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

# 2. Sales trend over time (if 'Date' column exists)
if 'Date' in data.columns:
    # Ensure 'Date' is a datetime column
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Group sales by date
    sales_trend = data.groupby('Date')['Sales'].sum()
    
    plt.figure(figsize=(10, 6))
    sales_trend.plot(color='green')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.show()
else:
    print("\nThe dataset does not have a 'Date' column.")

# 3. Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
