import unittest
from django.test import Client

class SimpleTests(unittest.TestCase):
    
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
