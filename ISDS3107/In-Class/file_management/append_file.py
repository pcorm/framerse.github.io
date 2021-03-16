more_students = ["Sonja", "Melissa", "Karen", 'Joe Burrow', 'Evelyn', "Mr. Big"]
file = open("ISDS3107/output_file.txt", 'a')
file.write("Here is a list of names: \n")

for s in more_students:
    file.write(s + "\n")

file.close()
