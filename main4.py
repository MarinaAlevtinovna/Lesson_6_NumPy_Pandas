import pandas as pd

data = {
    'набор А': [85, 90, 95, 100, 105],
    'набор В': [70, 80, 95, 110, 120]
}
df = pd.DataFrame(data)

stdA = df['набор А'].std()
stdB = df['набор В'].std()

print(stdA)
print(stdB)