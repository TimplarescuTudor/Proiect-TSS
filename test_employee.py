import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Ion', 'Popescu', 50000)
        self.emp_2 = Employee('Andrei', 'Gheorghe', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Ion.Popescu@email.com')
        self.assertEqual(self.emp_2.email, 'Andrei.Gheorghe@email.com')

        self.emp_1.first = 'Ionut'
        self.emp_2.first = 'Andreea'

        self.assertEqual(self.emp_1.email, 'Ionut.Popescu@email.com')
        self.assertEqual(self.emp_2.email, 'Andreea.Gheorghe@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Ion Popescu')
        self.assertEqual(self.emp_2.fullname, 'Andrei Gheorghe')

        self.emp_1.first = 'Ionut'
        self.emp_2.first = 'Andreea'

        self.assertEqual(self.emp_1.fullname, 'Ionut Popescu')
        self.assertEqual(self.emp_2.fullname, 'Andreea Gheorghe')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()