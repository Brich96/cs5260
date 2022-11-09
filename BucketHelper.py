import boto3
import json

class BucketHelper():
    
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    
    def __init__(self):
        pass
    
    def _getBucket(self, bucket_name):
        return self.s3.Bucket(bucket_name)
    
    def listAllBuckets(self):
        b = self.s3_client.list_buckets()
        for item in b['Buckets']:
            print(item['Name'])
    
    # TODO: implement mass delete if needed
    # response = s3_client.delete_objects(
    #     Bucket=bucket_name,
    #     Delete={"Objects": [{"Key": "text/test7.txt"}, {"Key": "text/test8.txt"}]},
    # )
    
    def createItem(self, bucket_name, file_name, json_data):
        s3obj = self.s3.Object(bucket_name, file_name)
        response = s3obj.put(Body=(bytes(json.dumps(json_data).encode('UTF-8'))))
        return response
        
    def getBucketItems(self, bucket_name):
        return self._getBucket(bucket_name).objects.filter(MaxKeys=1)
        
    def prepWidget(self, widget):
        del widget['type']
        del widget['requestId']
        
        return widget
        
    def deleteItem(self, bucket_name, key):
        response = self.s3_client.delete_object(Bucket=bucket_name, Key=key)
        return response