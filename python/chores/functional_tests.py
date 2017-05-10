import requests
import unittest
import run
import time

class ChoresTest(unittest.TestCase):
    def setUp(self):
        self.app = run.app.test_client()

    def tearDown(self):
        loop = True
        while loop:
            r = self.app.get('/active')
            if(r.data.decode() == 'No'):
                loop = False
            else:
                time.sleep(5)

    def test_send_sms_no_delay(self):
        r = self.app.get('/test0')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data.decode(), 'Starting test0, sms is sent in 0 minute')

    @unittest.skip("actual delay")
    def test_send_sms_1_min_delay(self):
        r = self.app.get('/test1')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data.decode(), 'Starting test1, sms is sent in 1 minute')

    def test_error_if_no_chore_match(self):
        r = self.app.get('/noexist')
        self.assertEqual(r.status_code, 404)
        

if __name__ == '__main__':
    unittest.main()
