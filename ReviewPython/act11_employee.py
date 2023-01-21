# Activity 11-3 Employee 

class Employee():
    """ Class that stores the name and annual salary of the employee"""
    def __init__(self, firstname, lastname, annualSalary):
        """Initializaiton of the attributes needed"""
        self.firstName = firstname
        self.lastName = lastname
        self.annualSalary = annualSalary

    def give_raise(self, giveRaise=5000):
        """ This gives raise to the annual salary. The default raise is 5k"""
        self.annualSalary += giveRaise

