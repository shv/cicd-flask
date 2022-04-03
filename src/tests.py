import unittest
import app as tested_app
import json

class FlaskAppTEst(unittest.TestCase):
    def setUp(self) -> None:
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello world')

    def test_post_hello_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)

    def test_get_api_endpoint(self):
        r = self.app.get('/api')
        self.assertEqual(r.json, {'status': 'test'})

    def test_correct_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'name': 'Den', 'age': 100}))
        self.assertEqual(r.json, {'status': 'OK'})
        self.assertEqual(r.status_code, 200)

    def test_not_dict_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps([{'name': 'Den'}]))
        self.assertEqual(r.json, {'status': 'bad input'})
        self.assertEqual(r.status_code, 400)