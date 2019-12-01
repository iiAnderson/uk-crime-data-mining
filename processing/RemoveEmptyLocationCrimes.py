import csv


infile = "C:/Users/Matt/Downloads/2016-12/out.csv"
outfile = "../2014-15Crime.csv"
writer = csv.writer(open(outfile, "w+", newline=""))

with open(infile, "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:
        if row[4] != "" and row[5] != "":
            writer.writerow(row)

        i += 1
        if i % 100000 == 0:
            print("Processed " + str(i) + " rows")
    print("Empty locations removed successfully")
