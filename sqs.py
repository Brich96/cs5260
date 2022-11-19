import boto3
import requests
import json
sqs = boto3.resource('sqs')

queue = sqs.Queue(url='https://sqs.us-east-1.amazonaws.com/860368004749/cs5260-requests')
# queue.send_message(MessageBody='test')

# for message in queue.receive_messages(MaxNumberOfMessages=10, VisibilityTimeout=10, AttributeNames=['All']):
#     print(message.body)


url = 'https://b6rns1xgzj.execute-api.us-east-1.amazonaws.com/dev'

data = {"type":"create","requestId":"148b08f0-c5c7-4277-a161-c2e203ea63b6","widgetId":"4454eacd-506f-40b4-a529-23ac79cf7b79","owner":"Benny Boy","label":"ZN","description":"HBTSLLNJZRRRUZGLLEYJUPJKGMDCIWKE","otherAttributes":[{"name":"size","value":"842"},{"name":"width","value":"600"},{"name":"width-unit","value":"cm"},{"name":"length-unit","value":"cm"},{"name":"price","value":"39.55"},{"name":"quantity","value":"308"},{"name":"note","value":"KHVVHLOSFKCMXWGKFKEWMNFDBOXUEOGXRNASOIPIYDNRWSICETNTEMYFIIAEYIIODPIFEECZGSHGNBVPMWNULOTDZGEHYVQKIJXHBFLKHQFBKVRGDFIRJTKZUXBTBDVPKUNXSALWPPAYFSNLITAQYIHEIJWXGUIMAGJMJUTHQSYQAQQPUHKCTDDWOMKFTGLFFCDMWNMZXDGUCJXRPWKRXEOUXSBYYRTNTUDVGPJHSFLUQTPFOFKMMJJHQRTWPTZVRBDYVOYQHMRYSUIEFLSXOABXRGRRLWELURLCRACOVZDFOMHEPPUSXNZNYXROIFNVRPKFCJWWNTTFCIZBLJLJRGSLUYNFEIMQSBTVNBHJOZMCSSJNZWDKLOWZMEPLUWWFIMCPMXULZEFN"}]}

# get_response = requests.get(url, json=data)

response = requests.post(url, json=data)

# print(get_response.text)
print(response.text)

# Clear out queue when done testing
# for message in queue.receive_messages(MaxNumberOfMessages=10, VisibilityTimeout=10, AttributeNames=['All']):
#     print(message.body)
    
#     message.delete()