import csv


file_path = "users.csv"

with open(file_path, "w") as f:
    f.write("Name,Username,Email\n"
			"Roger Smith,rsmith,wigginsryan@yahoo.com\n"
			"Michelle Beck,mlbeck,hcosta@hotmail.com\n"
			"Ashley Barker,a_bark_x,a_bark_x@turner.com\n"
			"Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com\n")

with open(file_path, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Email"])

# it is recommended to specify newline="" while opening csv files