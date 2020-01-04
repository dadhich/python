# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 08:18:18 2020

@author: Abhishek Dadhich
"""
import pandas as pd, numpy as np, matplotlib.pyplot as plt

df = pd.read_csv("C:\\AbhishekDadhichCodes\\Python\\python\\datasets\\diabetes.csv")

df.describe()
df.columns

# box plot
df["Pregnancies"].plot(kind="box")
df["Glucose"].plot(kind="box")
plt.boxplot(df["Glucose"],showmeans=True)
plt.boxplot(df["Age"],showmeans=True)

# histograms
df["Pregnancies"].plot(kind="hist")
plt.hist(df["Pregnancies"],bins=10)

# statistics
avg = df["Pregnancies"].mean()
variance= df["Pregnancies"].var()
std_dev = df["Pregnancies"].std()

(std_dev/avg)*100
skew = df["Pregnancies"].skew()
kurt = df["Pregnancies"].kurtosis()