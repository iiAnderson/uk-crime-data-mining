import csv, math

pop = {}
lsoa = {}

writer = csv.writer(open("dat.csv", "w"))

with open("lsoatopostcode.csv", "r") as f1:

    reader = csv.reader(f1)

    for row in reader:

        lsoa[row[1]] = row[3]

    print("Processed all lsoa codes")


with open("alldeprivation.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:

        lsoa_code = row[0].split("/")[(len(row[0].split("/"))-1)]
        pop[lsoa_code] = row[2]


with open("newdata.csv", "r") as f:

    reader = csv.reader(f)
    i=0

    for row in reader:

        r = []

        for p in row:
            r.append(p)

        if row[3] in pop.keys():
            r.append(pop[row[3]])

            writer.writerow(r)

        i += 1

        if i % 10000 == 0:
            print("Completed " + str(i))




