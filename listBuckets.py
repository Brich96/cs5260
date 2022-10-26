import boto3
import time
import json
from helper import BucketHelper




    
session = boto3.Session()
s3_client = session.client('s3')

bucketHelper = BucketHelper()
# bucketHelper.listAllBuckets()
    



    

def handleRequests():

    while True:
    
        bucketItems = bucketHelper.getBucketItems('usu-cs5260-waffle-requests')
        
        atLeastOneItem = False
        for obj in bucketItems:
            atLeastOneItem = True
            widget = json.loads(obj.get()['Body'].read())
            print(obj.key)
            
            if(widget['type'] == 'create'):
                
                # Remove uneeded keys
                del widget['type']
                del widget['requestId']
                
                # upload and delete request
                file_name = 'widgets/' + widget['owner'].lower().replace(" ", "-") + widget['widgetId']
                bucketHelper.uploadItem('usu-cs5260-waffle-web', file_name, widget)
                bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
            
            # TODO: implement change and delete
            
        if not atLeastOneItem:
            print("No Requests Yet")
            time.sleep(.2)
            
            
            
        
    
handleRequests()