try:
    my_file = open("/Users/cj/com728/week5/months.txt")

    for line in my_file.readlines():
        print(line)

    my_file.close()
except IOError:
    print("Cannot read file")


file_path = "/Users/cj/com728/week5/data_files/languages.txt"

try:
    with open(file_path) as my_file:
        lines = my_file.readlines()

    for line in lines:
        print(line)
    
except IOError:
    print("Cannot read file")
