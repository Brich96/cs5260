import boto3
import json



s3 = boto3.resource('s3')
    
session = boto3.Session()
s3_client = session.client('s3')
    
def listClient():
    b = s3_client.list_buckets()
    for item in b['Buckets']:
        print(item['Name'])

# listClient()

def deleteItem(bucket_name, key):
    response = s3_client.delete_object(Bucket=bucket_name, Key=key)
    print(response)
    return response
    
    # response = s3_client.delete_objects(
    #     Bucket=bucket_name,
    #     Delete={"Objects": [{"Key": "text/test7.txt"}, {"Key": "text/test8.txt"}]},
    # )
    
def uploadWidget(bucket_name, file_name, json_data):
    s3obj = s3.Object(bucket_name, file_name)
    
    s3obj.put(Body=(bytes(json.dumps(json_data).encode('UTF-8'))))
    

def getBucket():

    bucket = s3.Bucket('usu-cs5260-waffle-requests')
    for obj in bucket.objects.filter(MaxKeys=1).limit(1):
        widget = json.loads(obj.get()['Body'].read())
        print(widget)
        print(obj.key)
        if(widget['type'] == 'create'):
            del widget['type']
            del widget['requestId']
            file_name = 'widgets/' + widget['owner'].lower().replace(" ", "-") + widget['widgetId']
            uploadWidget('usu-cs5260-waffle-web', file_name, widget)
        # deleteItem('usu-cs5260-waffle-requests', obj.key)
        
    
getBucket()