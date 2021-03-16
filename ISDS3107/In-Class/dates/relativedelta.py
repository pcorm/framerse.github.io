from datetime import datetime
from dateutil.relativedelta import relativedelta

def main():
    birth_date = input('Enter your DOB as mm/dd/YYYY: ')
    print('your age is', age(birth_date))

def age(d):
    dob = datetime.strptime(d, '%m/%d/%Y')
    today = datetime.today()
    age = relativedelta(today, dob)
    return age.years

main()
