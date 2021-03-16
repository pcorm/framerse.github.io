from datetime import datetime

timestamp = datetime.fromtimestamp(1326244364)
print( "Date =", timestamp )

dob = datetime(2000, 1, 3, 2, 54)
print(dob)

t = dob.timestamp()
print("The timestamp of your birthday is: ", round(t))
