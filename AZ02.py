import pandas as pd
import matplotlib.pyplot as plt

data = {
    'name': ['Алексей', 'Марина', 'Иван', 'Ольга', 'Сергей', 'Екатерина', 'Андрей', 'Наталья', 'Дмитрий', 'Анна'],
    'math': [85, 90, 72, 88, 78, 91, 64, 82, 75, 89],
    'physics': [78, 85, 65, 92, 83, 89, 70, 88, 72, 94],
    'chemistry': [92, 79, 80, 94, 87, 95, 72, 91, 78, 97],
    'history': [74, 91, 68, 85, 70, 93, 66, 86, 73, 92],
    'literature': [88, 87, 75, 90, 82, 96, 68, 89, 76, 93]
}

df = pd.DataFrame(data)

print(df.head(5))

print(f'Средний балл по математике - {df['math'].mean()}')
print(f'Средний балл по физике - {df['physics'].mean()}')
print(f'Средний балл по химии - {df['chemistry'].mean()}')
print(f'Средний балл по истории - {df['history'].mean()}')
print(f'Средний балл по литературе - {df['literature'].mean()}')

print(f'Медианный балл по математике - {df['math'].median()}')
print(f'Медианный балл по физике - {df['physics'].median()}')
print(f'Медианный балл по химии - {df['chemistry'].median()}')
print(f'Медианный балл по истории - {df['history'].median()}')
print(f'Медианный балл по литературе - {df['literature'].median()}')

print(f'Стандартное отклонение по математике - {df['math'].std()}')
print(f'Стандартное отклонение по физике - {df['physics'].std()}')
print(f'Стандартное отклонение по химии - {df['chemistry'].std()}')
print(f'Стандартное отклонение по истории - {df['history'].std()}')
print(f'Стандартное отклонение по литературе - {df['literature'].std()}')


Q1 = df['math'].quantile(0.25)
Q3 = df['math'].quantile(0.75)
IQR = Q3 - Q1
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['math'] >= downside) & (df['math'] <= upside)]

df_new.boxplot(column='math')
plt.show()




