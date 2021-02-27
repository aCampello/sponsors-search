import os
import json

from convert_to_db import convert_to_db
from create_table import create_table
from get_data import get_data

import boto3


def _save_to_s3(path='.'):
    s3_client = boto3.client('s3')
    s3_client.upload_file(
        os.path.join(path, 'data.js'),
        os.environ['AWS_BUCKET'],
        'data.js'
    )

    s3_client.upload_file(
        os.path.join(path, 'sponsors.json'),
        os.environ['AWS_BUCKET'],
        'sponsors.json'
    )

    s3_client.upload_file(
        os.path.join(path, 'sponsors.csv'),
        os.environ['AWS_BUCKET'],
        'sponsors.csv'
    )


def handler(event, context):
    print("Reading data")
    get_data(path='/tmp')

    print("Parsing PDF")
    create_table(path='/tmp', verbose=False)

    print("Processing output")
    df_json = convert_to_db(path='/tmp')

    print("Saving to S3")
    _save_to_s3('/tmp')

    return {"message": "Success",
            "firstRecord": df_json[0]}

