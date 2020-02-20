import unittest
import pomodoro_logger
from datetime import datetime

class TestPomodoro(unittest.TestCase):
    def test_file_name(self):
        self.assertEqual(pomodoro_logger.file_name_with_date(datetime(1901,2,3)), '03-02-01.log')
    
    def test_log_exists(self):
        self.assertTrue(pomodoro_logger.log_exists('17-02-20.log'))

    def test_log_does_not_exist(self):
        self.assertFalse(pomodoro_logger.log_exists('blah.log'))

if __name__ == '__main__':
    unittest.main()