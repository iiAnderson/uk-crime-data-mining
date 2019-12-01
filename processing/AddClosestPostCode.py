import csv
import math

postcodes = {}

infile = "../2014-15Crime.csv"
postcodefile = "../lsoaToPostCode.csv"

with open(postcodefile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    i = 0
    for row in reader:
        # Assuming that the LSOA corresponds to the first postcode as one LSOA has multiple postcodes associated
        if row[3] not in postcodes.keys():
            postcodes[row[3]] = row[0]
        i += 1
        if i % 100000 == 0:
            print("Loaded " + str(i) + " postcode rows")

outfile = "../2014-15CrimeWithPostCodes.csv"
writer = csv.writer(open(outfile, "w+", newline=""))

with open(infile, "r") as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        # some rows don't have an LSOA code...
        if row[7] != "":
            row += [postcodes[row[7]]]
        i += 1
        writer.writerow(row)
        if i % 100000 == 0:
            print("Processed " + str(i) + " crime rows")






