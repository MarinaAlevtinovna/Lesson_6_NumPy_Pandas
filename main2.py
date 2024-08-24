import pandas as pd

df = pd.read_csv('lights.csv')

df['test'] = [new for new in range(36)] # Добавление нового столбца 'test'

# axis=1 - удаление столбцов, 0 - строк.
df.drop('test', axis=1, inplace=True) #удаление столбца
df.drop(35, axis=0, inplace=True) #удаление строки

# Сохранение изменений в другой файл CSV
df.to_csv('lights_modified.csv', index=False)

print(df)