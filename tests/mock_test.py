import unittest
import pandas as pd

class MockTest(unittest):
        def setUp(self):
              pass
        
        def mockT(self):
              self.assertEqual('me', 'me')
if __name__ == '__main__':
    unittest.main()