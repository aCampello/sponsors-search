FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
COPY app.py get_data.py convert_to_db.py create_table.py ./

RUN pip install -r requirements.txt

CMD ["app.handler"]
