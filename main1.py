import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head(3))
# print(df.tail(3))
# print(df.info())
# print(df.describe())
# print(df[['Country name', 'Regional indicator']])
# print(df.loc[56, 'Healthy life expectancy'])
print(df[df['Healthy life expectancy'] > 0.7])