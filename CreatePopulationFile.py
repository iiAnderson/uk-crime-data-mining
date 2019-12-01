import csv, math

pop = {}

writer = csv.writer(open("dat.csv", "w"))

with open("pop.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if not math.isnan(float(row[1].replace(",", ""))):
            pop[row[0]] = float(row[1].replace(",", ""))


with open("newdata.csv", "r") as f:

    reader = csv.reader(f)
    i=0

    for row in reader:


        r = []

        for p in row:
            r.append(p)

        if row[6].split(" ")[0] in pop.keys():
            r.append(pop[row[6].split(" ")[0]])

            writer.writerow(r)

        i += 1

        if i % 10000 == 0:
            print("Completed " + str(i))




