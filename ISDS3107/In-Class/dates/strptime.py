from datetime import datetime

#strptime stands for string parse time
#the word parse means analyzing a sentence into its parts and describing their syntactic roles
date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
