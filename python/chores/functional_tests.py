import requests
import unittest
import run

class ChoresTest(unittest.TestCase):
    def setUp(self):
        self.app = run.app.test_client()

    def test_send_sms(self):
        r = self.app.get('/test')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data.decode(), 'Starting test, sms is sent in 0 minute')

    def test_error_if_no_chore_match(self):
        r = self.app.get('/noexist')
        self.assertEqual(r.status_code, 404)
        

if __name__ == '__main__':
    unittest.main()
