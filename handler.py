import boto3
import time
import json
import sys
from BucketHelper import BucketHelper
from DynamoHelper import DynamoHelper
import logging

logging.basicConfig(filename="output.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

bucketHelper = BucketHelper()
dynamoHelper = DynamoHelper()

def handleRequests():

    while True:
        logger.info("Starting Consumer")
        bucketItems = bucketHelper.getBucketItems('usu-cs5260-waffle-requests')
        
        atLeastOneItem = False
        for obj in bucketItems:
            atLeastOneItem = True
            widget = json.loads(obj.get()['Body'].read())
            print(obj.key)
            logger.info(obj.key)
            
            if(widget['type'] == 'create'):
                
                # prep widget for insertion
                if(sys.argv[1] == 's3'):
                    prepped_widget = bucketHelper.prepWidget(widget)
                    
                    file_name = 'widgets/' + widget['owner'].lower().replace(" ", "-") + widget['widgetId']
                    bucketHelper.uploadItem('usu-cs5260-waffle-web', file_name, widget)
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                    
                elif(sys.argv[1] == 'dynamo'):
                    prepped_widget = dynamoHelper.prepWidget(widget)
                    dynamoHelper.createItem(widget)
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                
            else:
                bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
            
            # TODO: implement change and delete
            
        if not atLeastOneItem:
            print("No Requests Yet")
            time.sleep(.2)
            
            
            
        
    
handleRequests()