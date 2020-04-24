import pandas as pd

df_stock = pd.read_csv("../../data/raw/msft_stock_price.csv")
print(df_stock.head())
df_trends = pd.read_csv("../../data/raw/msft_google_trends.csv")
print(df_trends.head())

df_stock['Date'] = pd.to_datetime(df_stock['Date'])
df_stock['Year'] = df_stock['Date'].dt.year
df_stock['Week Number'] = df_stock['Date'].dt.week
print(df_stock.head())
df_trends['Week'] = pd.to_datetime(df_trends['Week'])
df_trends['Year'] = df_trends['Week'].dt.year
df_trends['Week Number'] = df_trends['Week'].dt.week
print(df_trends.head())

# Merging and Joining Data
df = pd.merge(df_stock, df_trends, on=['Year', 'Week Number'])
print(df.head())
pd.set_option('display.max_columns', None)

print(df.head())
df_stock.set_index('Year', inplace=True)
print(df_stock.head())

print(df_trends.head())
df = df_stock.join(df_trends, on='Year', lsuffix='_left', rsuffix='_right')
print(df.head())
