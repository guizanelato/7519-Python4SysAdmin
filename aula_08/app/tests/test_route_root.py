
import unittest 

from app import app as flaskapp

class TesteRotaRaiz(unittest.TestCase):
    def setUp(self):    
        app = flaskapp.test_client()
        self.response = app.get('/')

    def test_getRaiz(self):
        self.assertEqual(200, self.response.status_code)




