from datetime import datetime

# strftime stands for string from time
# this is if you have a date and you need to change it from one style to another

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%b/%Y, %H:%M:%S")
# dd/MMM/YY H:M:S format
print("s2:", s2)
