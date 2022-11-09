FROM python:3

COPY BucketHelper.py BucketHelper.py
COPY DynamoHelper.py DynamoHelper.py
COPY handler.py handler.py
COPY SQSHelper.py SQSHelper.py


RUN apt install curl

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

RUN pip3 install boto3

CMD ["python3", "handler.py", "s3", "s3"]