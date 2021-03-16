students = ["Jennifer", "Craig", "Robert", "Boudreaux", "Thibodeaux", "Texas", "Baton Rouge", "Apple"]
file = open("ISDS3107/output_file.txt", "w")
file.write("Here is a list of names: \n")

for s in students:
    file.write(s + "\n")

file.close()
