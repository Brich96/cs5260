import boto3
import time
import json
import sys
from BucketHelper import BucketHelper
from DynamoHelper import DynamoHelper
from SQSHelper import SQSHelper
import logging

if(not (len(sys.argv) > 1)):
    print("No Arguments...exiting")
    sys.exit()

logging.basicConfig(filename="output.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

bucketHelper = BucketHelper()
dynamoHelper = DynamoHelper()

#  TODO: items in web first

def handleRequests():

    while True:
        logger.info("Starting Consumer")
        
        #  TODO: have this be from queue or from s3
        if(sys.argv[2] == 's3'):
            bucketItems = bucketHelper.getBucketItems('usu-cs5260-waffle-requests')
        elif(sys.argv[2] == 'sqs'):
            sqshelper = SQSHelper()
            bucketItems = sqshelper.getItems()
        else:
            print("invalid arguments")
            sys.exit()
        
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
                    
                    file_name = 'widgets/' + prepped_widget['owner'].lower().replace(" ", "-") + prepped_widget['widgetId']
                    bucketHelper.createItem('usu-cs5260-waffle-web', file_name, prepped_widget)
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                    
                elif(sys.argv[1] == 'dynamo'):
                    prepped_widget = dynamoHelper.prepWidget(widget)
                    dynamoHelper.createItem(prepped_widget)
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                    
            elif(widget['type'] == 'update'):
                
                if(sys.argv[1] == 's3'):
                    prepped_widget = bucketHelper.prepWidget(widget)
                    
                    file_name = 'widgets/' + prepped_widget['owner'].lower().replace(" ", "-") + prepped_widget['widgetId']
                    bucketHelper.createItem('usu-cs5260-waffle-web', file_name, prepped_widget)
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                    
                elif(sys.argv[1] == 'dynamo'):
                    prepped_widget = dynamoHelper.prepWidget(widget)
                    dynamoHelper.deleteItem(prepped_widget['id'])
                    dynamoHelper.createItem(prepped_widget)
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                    
            elif(widget['type'] == 'delete'):
                
                if(sys.argv[1] == 's3'):
                    
                    file_name = 'widgets/' + widget['owner'].lower().replace(" ", "-") + widget['widgetId']
                    bucketHelper.deleteItem('usu-cs5260-waffle-web', file_name)
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                    
                elif(sys.argv[1] == 'dynamo'):
                    dynamoHelper.deleteItem(widget['widgetId'])
                    bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
                
            else:
                bucketHelper.deleteItem('usu-cs5260-waffle-requests', obj.key)
            
            # TODO: implement change and delete
            
        if not atLeastOneItem:
            print("No Requests Yet")
            time.sleep(.2)
            
            
            
        
    
handleRequests()