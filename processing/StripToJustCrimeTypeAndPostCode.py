import csv


infile = "../2014-15CrimeWithPostCodes.csv"
outfile = "../2014-15JustCrimeAndPostCodes.csv"
writer = csv.writer(open(outfile, "w+", newline=""))

with open(infile, "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:
        # some rows don't have postcodes
        if len(row) >= 13 and row[12] != "":
                writer.writerow([row[1], row[9], row[12]])

        i += 1
        if i % 100000 == 0:
            print("Processed " + str(i) + " rows")
    print("Empty locations removed successfully")
