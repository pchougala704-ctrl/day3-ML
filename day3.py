from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np

df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())

df.info()

print(df.shape)

print(df.isnull().sum())

print(df.describe())

print(df.duplicated().sum)

print(df.tail())

df["Age"].fillna(df["Age"].mean(),inplace=True)

df.isnull().sum()

df["Cabin"].fillna(df["Cabin"].mean(),inplace=True)

df["Cabin"].fillna(df["Cabin"].ffill(),inplace=True)

df.isnull().sum()

df["Embarked"].fillna(df["Embarked"].ffill(),inplace=True)

df.isnull().sum()

df.dropna()

df.drop("SibSp",axis=1,inplace=True)

df.duplicated()



