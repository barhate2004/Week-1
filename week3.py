import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data.csv")

print(df)

# View first 5 rows
print(df.head())

# View column names
print(df.columns)

# Basic information
print(df.info())

# Statistics
print(df.describe())

# Filter data
print(df[df["Calories"] > 400])



plt.plot(df["Duration"], df["Calories"])
plt.xlabel("Duration")
plt.ylabel("Calories")
plt.show()

sns.scatterplot(x="Pulse", y="Calories", data=df)
plt.show()