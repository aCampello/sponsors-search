import pandas as pd

df = pd.read_csv('data.csv', index_col=0)

import json

with open('data.js', 'w') as f:
    df_json = json.dump(df.to_dict(orient='records'), f)

