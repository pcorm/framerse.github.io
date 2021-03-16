# (1, 'Kristen', 'Klein', '2002-11-03', 'North Cynthiafurt', 'AZ', '50788')
# (2, 'April', 'Norman', '1993-08-25', 'Patrickshire', 'MN', '37010')
# (3, 'Justin', 'Hanna', '1998-01-30', 'North Chadfurt', 'WA', '39505')
# (4, 'Pamela', 'Stephens', '1995-11-12', 'Margaretland', 'MN', '13967')

from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

class Customer:
    student_name = "Patrick Cormier"

    def __init__(self, id, fname, lname, dob, city, state, zip):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.dob = dob
        self.city = city
        self.state = state
        self.zip = zip

    def full_name(self):
        return self.first_name + " " + self.last_name

    def age(self):
        dob = datetime.strptime(self.dob, '%Y-%m-%d')
        today = datetime.today()
        age = relativedelta(today, dob)
        return age.years

    def adult(self):
        return self.age() >= 18

# {"id": 1, "first_name": "Kristen", "last_name": "Klein", "dob": "2002-11-03", "city": "North
# Cynthiafurt", "state": "AZ", "zip": "50788", "age": 16, "full_name": "Kristen Klein", "adult":
# false}

    def to_json(self):
        j = {}
        j.update(self.__dict__)
        j['age'] = self.age()
        j['full_name'] = self.full_name()
        j['adult'] = self.adult()
        return j
