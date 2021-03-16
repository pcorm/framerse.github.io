class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def full_name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, employee_id):
        Person.__init__(self, first, last)
        self.employee_id = employee_id

    def employee_name(self):
        return self.full_name() + ", " +  str(self.employee_id)

# ***in terminal change directory to current, type "python"***
# >>> from class_inheritance import Person, Employee
# >>> type(e)
# <class 'class_inheritance.Employee'>
# >>> e = Employee("james", "davis", 87)
# >>> e.employee_name()
# 'james davis, 87'
