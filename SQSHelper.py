import boto3


class SQSHelper():
    
    
    def __init__(self):
        pass
    
    def getItems(self):
        sqs = boto3.resource('sqs')

        # queue = sqs.get_queue_by_name(QueueName='cs5260-requests')
        
        queue = sqs.Queue('https://queue.amazonaws.com/860368004749/cs5260-requests')
        
        items = []
        for message in queue.receive_messages(MaxNumberOfMessages=10, VisibilityTimeout=10, AttributeNames=['All']):
            items.append(message.body)
            
            message.delete()
        return items
    
    def deleteItems(self):
        sqs = boto3.resource('sqs')
        queue = sqs.Queue('https://queue.amazonaws.com/860368004749/cs5260-requests')
        for message in queue.receive_messages(MaxNumberOfMessages=10, VisibilityTimeout=10, AttributeNames=['All']):
            print(message.body)
            
            message.delete()
                
    