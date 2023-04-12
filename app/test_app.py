import unittest
from routes import application

class TestMyApp(unittest.TestCase):
    
    def setUp(self):
        self.client = application.test_client()
        
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Python Flask App</h1>', response.data)

if __name__ == '__main__':
    unittest.main()