import pandas as pd
import json

df = pd.read_csv('noc-cnp.csv')
nocdf = df.groupby('Code',  sort=True,  as_index=False).agg(
    {'Element Description English': lambda x: list(x)})  
nocdf = nocdf.rename({'Code': 'code', 'Element Description English': 'job_titles'}, axis=1)
noc_json = nocdf.to_json(orient='records')
noc_parsed= json.loads(noc_json)

with open('noc.json', 'w') as file:
    json.dump(noc_parsed, file, indent=4)
