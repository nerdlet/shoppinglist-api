import unittest
import os
import json
from app import create_app, db

class ShoppingListTestCase(unittest.TestCase):

    
    def setUp(self):
    	"""before tables are creates"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.shoppinglist = {'name': 'apples'}
        with self.app.app_context():
            db.create_all()

    """after tabels are created"""
    def tearDown(self):
    	with self.app.app_context():
    		db.session.remove()
    		db.drop_all()

#make tests executable
if __name__ == "__main__":
	unittest.main()