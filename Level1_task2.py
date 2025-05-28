# -*- coding: utf-8 -*-
"""
Created on Mon May 26 17:23:44 2025

@author: jainp
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("E:/intern/codveda/2) Stock Prices Data Set.csv", parse_dates=['date'])

# ---------------------------
# 1. Summary Statistics
# ---------------------------
summary_stats = df.describe(include='all')
mode_values = df.mode().iloc[0]
median_values = df.median(numeric_only=True)

print("Summary Statistics:\n", summary_stats)
print("\nMedian Values:\n", median_values)
print("\nMode Values:\n", mode_values)

# ---------------------------
# 2. Visualizations
# ---------------------------

# Set general plot style


# Histogram of closing prices
plt.figure(figsize=(8, 5))
sns.histplot(df['close'], bins=30, kde=True)
plt.title("Distribution of Closing Prices")
plt.xlabel("Close Price")
plt.ylabel("Frequency")
plt.show()

# Boxplot of stock prices
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['open', 'high', 'low', 'close']])
plt.title("Boxplot of Stock Price Features")
plt.ylabel("Price")  
plt.show()

# Scatter plot: Open vs Close
plt.figure(figsize=(5, 5))
sns.scatterplot(x='open', y='close', data=df, hue='symbol', alpha=0.7)
plt.title("Open vs Close Prices")
plt.xlabel("Open")
plt.ylabel("Close")
plt.show()

# ---------------------------
# 3. Correlation Matrix
# ---------------------------
plt.figure(figsize=(8, 6))
correlation = df[['open', 'high', 'low', 'close', 'volume']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()
