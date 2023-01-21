# Activity 11-3 Employee (Test case)

# importing the package needed so we can test a class
import unittest

# This is the class we need to test
from act11_employee import Employee

class TestEmployeeClass(unittest.TestCase):
    """ This class is to test Employee class from act 11"""
    
    def setUp(self):
        """ Setiing up instance here """
        self.employee = Employee("keiji", "plata", 5000)

    def test_give_default_raise(self):
        """ Testing if the method is capable of giving default raise """
        self.employee.give_raise()
        self.assertEqual(self.employee.annualSalary, 10_000)

    def test_give_custom_raise(self):
        """ Testing if the method is capable of giving custom raise """
        self.employee.give_raise(1)
        self.assertEqual(self.employee.annualSalary, 5001)

if __name__ == '__main__':
    unittest.main()
    
    
