import unittest
from chores import Chores

class ChoresTest(unittest.TestCase):
    def test_test_chore_exists(self):
        self.assertEqual(Chores.get_delay('test'), 1)

    def test_test_chore_doesnt_exist(self):
        self.assertEqual(Chores.get_delay('noexist'), -1)

if __name__ == '__main__':
    unittest.main()
