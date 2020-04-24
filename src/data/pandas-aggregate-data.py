import pandas as pd

df = pd.read_csv("../../data/raw/AAPL.csv")
print(df.head())

print(df['Open'].pct_change().head())
print(df['High'].pct_change().head())
print(df['Low'].pct_change().head())
print(df['Close'].pct_change().head())
print(df[["Open", "High", "Low", "Close"]].pct_change().head())
df['Returns'] = ((df['Close'] - df['Open']) / df['Open']) * 100.0
print(df.head())
print(df['Returns'].pct_change().head())

print(df.cov().head())
print(df.corr().head())
print(df['Open'].cumsum().head())
print(df['Open'].rolling(window=5).mean().head(20))
print(df['Open'].rolling(window=10).mean().head(20))
