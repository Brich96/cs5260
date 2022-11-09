import boto3
import json

class DynamoHelper():
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('widgets')
    
    def __init__(self):
        pass
    
    def listAllItems(self):
        response = self.table.scan()
        print(response)
        for i in response['Items']:
            print(i)
    
    def createItem(self, widget):
        self.table.put_item(Item=widget)
        
    def prepWidget(self, widget):
        del widget['type']
        del widget['requestId']
        
        for att in widget['otherAttributes']:
            widget[att['name']] = att['value']

        del widget['otherAttributes']
        
        widget['id'] = widget.pop('widgetId')
        
        return widget
        
    def deleteItem(self, itemId):
        response = self.table.delete_item(
                Key={
                    'id': itemId
                }
            )
        
        return response