# Exploratory data analysis on fraud data
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clean/creditcard_clean.csv")

print(df.info())
print(df.shape)
print(df.head())

counts = df['Class'].value_counts(normalize=True)
print(counts)
print(f"Fraudulent transactions: {counts[1] / counts.sum():.4%}")

labels = ['Legitimate (0)', 'Fraudulent (1)']
sns.countplot(x='Class', data=df)
plt.yscale('log')
plt.title("Class Distribution: 0 = Legitimate, 1 = Fraudulent")
plt.savefig("../data/exploratory_analysis/Class_Count_Plot.pdf")

plt.figure(figsize=(6, 6))
plt.pie(counts, labels=labels, autopct='%1.4f%%', startangle=90, colors=["skyblue", "salmon"])
plt.title("Fraudulent vs Legitimate Transactions")
plt.savefig("../data/exploratory_analysis/Class_Dist_Pie.pdf")

