import unittest
from BucketHelper import BucketHelper
from SQSHelper import SQSHelper
import requests
import json

class TestAll(unittest.TestCase):
    
    def test_bucket_helper_list_buckets(self):
        bhelper = BucketHelper()
        
        try:
            bhelper.listAllBuckets()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        
        
    def test_sqs_helper_get_items(self):
        sqsHelper = SQSHelper()
        
        try:
            items = sqsHelper.getItems()
            print(items)
            self.assertTrue(True)
        except:
            self.assertFalse(False)
    
    def test_sqs_helper_gets_correct_items(self):
        sqsHelper = SQSHelper()
        sqsHelper.deleteItems()
        
        url = 'https://b6rns1xgzj.execute-api.us-east-1.amazonaws.com/dev'

        data = {
            "test": "worked",
            "test2": "working"
        }
        
        requests.post(url, json=data)
        items = sqsHelper.getItems()
        
        self.assertTrue(json.loads(items[0]) == data)

        
        
if __name__ == '__main__':
    unittest.main()