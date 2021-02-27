import datetime

import os
import json

import pandas as pd


def convert_to_db(path='.'):
    df = pd.read_csv(os.path.join(path, 'sponsors.csv'), index_col=0)

    df_json = df.to_dict(orient='records')
    with open(os.path.join(path, 'data.js'), 'w') as f:
        f.write(f'var when = \"{datetime.datetime.utcnow().strftime("%d/%m/%Y")}\"\n')
        f.write('var data = ')
        json.dump(df_json, f)

    with open(os.path.join(path, 'sponsors.json'), 'w') as f:
        json.dump(df_json, f)

    return df_json


if __name__ == "__main__":
    convert_to_db()
