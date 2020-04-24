import pandas as pd

df_2015 = pd.read_csv('../../data/raw/tesla_2015.csv')
print(df_2015.head())
del df_2015['Unnamed: 0']
print(df_2015.head())
df_2016 = pd.read_csv('../../data/raw/tesla_2016.csv')
print(df_2016.head())
del df_2016['Unnamed: 0']
print(df_2016.head())
df_2017 = pd.read_csv('../../data/raw/tesla_2017.csv')
print(df_2017.head())
del df_2017['Unnamed: 0']
print(df_2017.head())
df_2018 = pd.read_csv('../../data/raw/tesla_2018.csv')
print(df_2018.head())
del df_2018['Unnamed: 0']
print(df_2018.head())

# Concatenating Files with Pandas
li = [df_2015, df_2016, df_2017, df_2018]
combined_df = pd.concat(li, axis=0, ignore_index=True)
print(combined_df.head())
combined_df.loc[:, 'datetime'] = pd.to_datetime(combined_df['Week'])
combined_df.loc[:, 'year'] = combined_df['datetime'].dt.year
print(set(combined_df['year'].values))

# Writing Concatenated Files to CSV with Pandas
combined_df.to_csv("../../data/interim/combined_tesla_files.csv")
df = pd.read_csv("../../data/interim/combined_tesla_files.csv")
del df['Unnamed: 0']
print(df.head())
print(set(df['year'].values))