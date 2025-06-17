# Exploratory data analysis on fraud data
import matplotlib as mpl
import seaborn as sns

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clean/creditcard_clean.csv")

print(df.info())
print(df.shape)
print(df.head())
print(df['Class'].value_counts(normalize=True))

