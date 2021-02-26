python3 get_data.py
python3 create_table.py
python3 convert_to_db.py

aws s3 cp sponsors.csv $S3_BUCKET --acl public-read
aws s3 cp sponsors.json $S3_BUCKET --acl public-read
aws s3 cp data.js $S3_BUCKET --acl public-read
