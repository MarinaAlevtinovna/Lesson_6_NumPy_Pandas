import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

data = {
    'Name' : ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age' : [25, 45, 25, 22],
    'City' : ['New York', 'Moscow', 'LA', 'Berlin']
}

df = pd.DataFrame(data)
print(df)