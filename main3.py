import pandas as pd

df = pd.read_csv('test.csv')
print(df)

#Заполняем NaN - пропуски в таблице файла
df.fillna(0, inplace=True)
df.to_csv('test.csv', index=False)
#Удаляем строки с NaN
#df.dropna(inplace=True)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()

print(group)