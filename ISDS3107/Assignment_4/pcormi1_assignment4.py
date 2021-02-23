import csv

student_name = "Patrick Cormier"

sum_city_mileages = 0
count_city_mileages = 0
sum_hwy_mileages = 0
count_hwy_mileages = 0
sum_ford_highway_mileages = 0
count_ford_highway_mileages = 0
sum_suv_city_mileages = 0
count_suv_highway_mileages = 0

mpg_file = open("mpg.csv", "r")
mpg_reader = csv.reader(mpg_file)
next(mpg_reader)
for row in mpg_reader:
    sum_city_mileages += float(row[8])
    count_city_mileages += row.count(row) + 1
    sum_hwy_mileages += float(row[9])
    count_hwy_mileages += row.count(row) + 1
    if row[1] == 'ford':
        sum_ford_highway_mileages += float(row[9])
        count_ford_highway_mileages += row.count(row) + 1
    if row[11] == 'suv':
        sum_suv_city_mileages += float(row[8])
        count_suv_highway_mileages += row.count(row) + 1

avg_city = sum_city_mileages / count_city_mileages
avg_hwy = sum_hwy_mileages / count_hwy_mileages
ford_hwy = sum_ford_highway_mileages / count_ford_highway_mileages
suv_city = sum_suv_city_mileages / count_suv_highway_mileages

output_file = open("pcormi1_assignment4.txt", "w")
output_file.write("The average city mileage for all vehicles is: " + str(avg_city) +
"\nThe average highway mileage for all vehicles is: " + str(avg_hwy) +
"\nThe average highway mileage for all Ford vehicles is: " + str(ford_hwy) +
"\nThe average city mileage for all SUV vehicles is: " + str(suv_city))

output_file.close()
mpg_file.close()
