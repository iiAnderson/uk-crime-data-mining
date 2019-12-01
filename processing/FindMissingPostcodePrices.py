import csv

postcodes = {}
postcodepricefile = "../data/averagepricebypostcode.csv"
postcodefile = "../data/postcodes.csv"

with open(postcodepricefile, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        postcodes[row[0]] = row[1]

counter = 0
total_postcodes = 0

# print "=============================="
# print "||    Missing Postcodes     ||"
# print "=============================="
with open(postcodefile, "r") as f2:
    reader2 = csv.reader(f2)
    for row2 in reader2:
        if row2[12] == "England" or row2[12] == "Wales":
            total_postcodes = total_postcodes+1
            if row2[0] not in postcodes:
                counter=counter+1
    #             print row2[0]

print "Total " + str(counter) + " missing out of " + str(total_postcodes) + " (" + str(float(counter)/total_postcodes*100) + "%)"