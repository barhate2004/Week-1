import pandas as pd

df = pd.read_excel("SQL_Sales_Dataset_200_Rows.xlsx")

print(df.head())
print(df.info())

#Handle missing values and duplicates
print(df.describe())
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()

#Group by category and find total revenue
revenue = df.groupby("category")["total_price"].sum()
print(revenue)

#Sort by multiple columns
df_sorted = df.sort_values(
    by=["category", "total_price"],
    ascending=[True, False]
)

print(df_sorted)

#Create a correlation matrix
correlation = df.corr(numeric_only=True)

print(correlation)