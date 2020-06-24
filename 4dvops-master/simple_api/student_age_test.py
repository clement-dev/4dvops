import unittest
from student_age import get_password 

class MyTest(unittest.TestCase):
    def test_get_password(self):
        self.assertAlmostEqual(get_password('toto'), 'python')
        self.assertAlmostEqual(get_password('tata'), None)

if __name__ == '__main__':
    unittest.main()