import sqlalchemy as db
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

student_name = "Patrick Cormier"
# (1, 'Kristen', 'Klein', '2002-11-03', 'North Cynthiafurt', 'AZ', '50788')
# (2, 'April', 'Norman', '1993-08-25', 'Patrickshire', 'MN', '37010')
# (3, 'Justin', 'Hanna', '1998-01-30', 'North Chadfurt', 'WA', '39505')
# (4, 'Pamela', 'Stephens', '1995-11-12', 'Margaretland', 'MN', '13967')

# "[1, 'Kristen Klein', 18]"
# "[2, 'April Norman', 27]"
# "[3, 'Justin Hanna', 23]"

def main():
    engine = db.create_engine('sqlite:///customer.sqlite')
    connection = engine.connect()
    results = connection.execute('select * from customer')

    out_file = open('pcormi1_assignment5.csv', 'w')
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(["Customer ID", "Name", "Age"])
    for row in results:
        csv_writer.writerow([row[0], full_name(row[1], row[2]), age(row[3])])

    connection.close()
    out_file.close()

def full_name(fname, lname):
    return fname + ' ' + lname

def age(d):
    dob = datetime.strptime(d, '%Y-%m-%d')
    today = datetime.today()
    age = relativedelta(today, dob)
    return age.years

main()
