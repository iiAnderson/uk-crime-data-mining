import csv

# outfile = "data/out/housepricecleanedwithlatlong2.csv"
writer = csv.writer(open("out.csv", "w", newline=""))

lsoa = {}

# print("Loading postcodes")
# postcode = open("averagepricebypostcode.csv", "r")
# postreader = csv.reader(postcode)
# for prow in postreader:
#     postcodes[prow[0].replace(" ", "").lower()] = prow[1]
#
# print("Loaded postcodes")
#

# CONVERTS LSOA POSTCODES TO THE CORRESPONDING POSTCODE (CREATES AveragePriceByLSOA.csv)
# with open("lsoatopostcode.csv", "r") as f:
#     reader = csv.reader(f)
#
#     print("Success: Dataset Loaded")
#
#     i = 0
#     for row in reader:
#
#         if row != [] and i != 0:
#             postc = row[1]
#             lsoa = row[3]
#
#             if postc.replace(" ", "").lower() in postcodes.keys():
#
#                 writer.writerow([postc, postcodes[postc.replace(" ", "").lower()], lsoa])
#
#         i += 1
#
#         if i % 1000 == 0:
#             print("Processed " + str(i))


# Counts the number of rows
# with open("doneshit.csv", "r") as f:
#     reader = csv.reader(f)
#     print("Success: Dataset Loaded")
#
#     i = 0
#     for row in reader:
#         i += 1
#
#         print(row)
#
#         if i > 9998:
#             break
#
#         if i % 1000 == 0:
#             print("Processed " + str(i))
#
print("Loading postcodes")
lsoa_file = open("AveragePriceByLSOA.csv", "r")
lsoareader = csv.reader(lsoa_file)
for prow in lsoareader:
    lsoa[prow[0].replace(" ", "").lower()] = prow[1]

print("Loaded postcodes")

with open("training_set.csv", "r") as f:
    reader = csv.reader(f)

    print("Success: Dataset Loaded")

    i = 0
    for row in reader:

        if row != [] and i != 0:
            lsoa_code = row[6]

            if lsoa_code.replace(" ", "").lower() in lsoa.keys():
                a = []
                for p in row:
                    a.append(p)
                a.append(lsoa[lsoa_code.replace(" ", "").lower()])
                writer.writerow(a)

        i += 1

        if i % 10000 == 0:
            print("Processed " + str(i))

#
#

#
# with open("AverageHousePriceWithLSOA.csv", "r") as f:
#     reader = csv.reader(f)
#
#     print("Success: Dataset Loaded")
#
#     i = 0
#     for row in reader:
#
#         if row != [] and i != 0:
#             lsoa_code = row[2]
#
#             if lsoa_code in lsoa.keys():
#                 val = lsoa[lsoa_code]
#
#                 lsoa[lsoa_code] = [float(val[0])+float(row[1]), val[1]+1]
#             else:
#                 lsoa[lsoa_code] = [float(row[1]), 1]
#
#         i += 1
#         #
#         # if i % 1000 == 0:
#         #     print("Processed " + str(i))
#
#     for key in lsoa.keys():
#         print("writing")
#         writer.writerow([key, (lsoa[key][0]/lsoa[key][1])])