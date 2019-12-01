import csv

outfile = "data/out/averagelatlong.csv"
writer = csv.writer(open(outfile, "w+"))

postcode_lookup = {}

print("---------------")
print("Loading Postcode CSV")

with open("data/postcodes.csv", "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:
        postcode_lookup[row[0]] = [row[2], row[3]]
        i += 1

        if i % 100000 == 0:
            print("Processed " + str(i) + " postcodes")
    print("Postcodes Loaded successfully")

print("---------------")
print("Loading House price data")

with open("data/out/averagepricebypostcode.csv", "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:

        out_row = []

        # Price
        out_row.append(row[1])

        # Postcode
        out_row.append(row[0])


        try:
        # Latitude
            latlong = postcode_lookup[row[0]]


            out_row.append(latlong[0])

            # Longditude
            out_row.append(latlong[1])

            writer.writerow(out_row)
        except KeyError:
            print("Postcode " + row[0] + " cannot be located")



        i += 1
        if i % 100000 == 0:
            print("Processed " + str(i) + " rows")

    print("Dataset Created successfully, location " + outfile)
    print("---------------")
