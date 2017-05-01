from selenium import webdriver
import unittest

class ChoresTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_send_sms(self):
        self.browser.get('http://localhost:5000/')

if __name__ == '__main__':
    unittest.main()
