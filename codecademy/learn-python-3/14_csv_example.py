import csv


file_path = "addresses.csv"

# since commas are used to separate the same data (address),
#  we must use a different delimiter to separate different data
#  in this example, we will use ";"

with open(file_path, newline="") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        print(row)

# it is recommended to specify newline="" while opening csv files