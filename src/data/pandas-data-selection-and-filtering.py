import pandas as pd

df = pd.read_csv('../../data/raw/aac_shelter_outcomes.csv')

print(df.head())
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.head())

# simple columns selection
df_select = df[['animal_type', 'color', 'breed']]
print(df_select.head())
print(df_select.head(20))

# datetime transformation
df.loc[:, 'date_of_birth'] = pd.to_datetime(df['date_of_birth'])
df.loc[:, 'week'] = df['date_of_birth'].dt.week
print(df.head())
df.loc[:, 'month'] = df['date_of_birth'].dt.month
df.loc[:, 'year'] = df['date_of_birth'].dt.year
print(df.head())
df_select = df[['year', 'month', 'week', 'sex_upon_outcome']]
print(df_select.head())

# simple querying
print(set(df_select['year'].values))
df_select = df_select[df_select['year'] < 2010]
print(set(df_select['year'].values))
print(set(df_select['sex_upon_outcome'].values))
df_select_new = df_select[df_select['sex_upon_outcome'] == 'Intact Male']
print(set(df_select_new['sex_upon_outcome'].values))
df_select_new = df_select[df_select['sex_upon_outcome'].isin(['Spayed Female', 'Intact Male'])]
print(set(df_select_new['sex_upon_outcome'].values))
