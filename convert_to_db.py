import pandas as pd
import json

df = pd.read_csv('sponsors.csv', index_col=0)
print(f"Data has {len(df)} entries")
df_json = df.to_dict(orient='records')
with open('data.js', 'w') as f:
    f.write('var data = ')
    json.dump(df_json, f)

with open('sponsors.json', 'w') as f:
    json.dump(df_json, f)
