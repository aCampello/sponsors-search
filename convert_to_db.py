import pandas as pd
import json

df = pd.read_csv('data.csv', index_col=0)

df_json = df.to_dict(orient='records')
with open('data.js', 'w') as f:
    f.write('var data = ')
    json.dump(df_json, f)

with open('sponsors.json', 'w') as f:
    json.dump(df_json, f)
