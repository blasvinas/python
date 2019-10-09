import unittest

from employee import Employee

class EmployeeTestcase(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Blas','Vinas',20000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        salary = self.my_employee.get_salary()
        self.assertEqual(salary,25000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        salary = self.my_employee.get_salary()
        self.assertEqual(salary,30000)
    
unittest.main()