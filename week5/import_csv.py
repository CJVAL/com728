import csv

file_path = ("/Users/cj/com728/week5/practice_files/username_password.csv")

try:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row)

except IOError:
    print("Error! Cannot read file!")