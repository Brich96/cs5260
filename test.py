import unittest
from BucketHelper import BucketHelper

class TestAll(unittest.TestCase):
    
    def test_bucket_helper_list_buckets(self):
        bhelper = BucketHelper()
        
        try:
            bhelper.listAllBuckets()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        
        
        
if __name__ == '__main__':
    unittest.main()