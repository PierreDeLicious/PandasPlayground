import pandas as pd
from collections import Counter

df = pd.read_csv("../../data/raw/fifa_19.csv")
print(df.head())
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = df[['Name', 'Age', 'Nationality', 'Preferred Foot', 'Height', 'Weight', 'Position', 'Overall']]
print(df.head())

print("Mean Height (cm): ", df['Height'].mean())
print("Mean Weight (kg): ", df['Weight'].mean())
print("Standard Deviation Height (kg): ", df['Height'].std())
print("Standard Deviation Weight (kg): ", df['Weight'].std())
print("Minimum Height (kg): ", df['Height'].min())

print("Maximum Height (kg): ", df['Height'].max())
print("Minimum Weight (kg): ", df['Weight'].min())
print("Maximum Weight (kg): ", df['Weight'].max())

# Generating Statistics from Categorical Columns
print("Mode of Nationality: ", df['Nationality'].mode())
print("Mode of Position: ", df['Position'].mode())
print("Mode of Preferred Foot: ", df['Preferred Foot'].mode())

print(Counter(df['Nationality']))
print(Counter(df['Nationality']).most_common(5))
print(Counter(df['Position']).most_common(5))
print(Counter(df['Preferred Foot']).most_common(5))