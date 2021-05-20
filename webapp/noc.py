import pandas as pd

df = pd.read_csv('noc-cnp.csv')
df.groupby('Code',  sort=True)

print("data frame", df)