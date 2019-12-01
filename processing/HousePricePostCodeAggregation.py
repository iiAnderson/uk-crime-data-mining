import csv
import sys
from dateutil import parser

in_csv = sys.argv[1]

postcodes = {}

yearly_inflation_rates = {
    2017 : 1.0294,
    2016 : 1.016,
    2015: 1.002,
    2014 : 1.005,
    2013 : 1.0199,
    2012 : 1.0271,
    2011 : 1.0420,
    2010 : 1.0373,
    2009 : 1.0283,
    2008 : 1.0311,
    2007 : 1.0212,
    2006 : 1.0297,
    2005 : 1.0192,
    2004 : 1.0164,
    2003 : 1.0125,
    2002 : 1.0169,
    2001 : 1.0107,
    2000 : 1.0075,
    1999 : 1.0120,
    1998 : 1.0155,
    1997 : 1.0169,
    1996 : 1.0230,
    1995 : 1.0296,
    1994 : 1.0205,
    1993 : 1.0248
}


def recursive_inflation (year):
    if year == 2017:
        return yearly_inflation_rates[2017]
    else:
        return yearly_inflation_rates[year] * recursive_inflation(year+1)

with open(in_csv, "r") as f:
    reader = csv.reader(f)

    i = 0
    for row in reader:
        date = parser.parse(row[2])
        year = int(date.year)
        inflated_price = int(row[1]) * recursive_inflation(year)

        if row[3] in postcodes.keys():

            postcodes[row[3]].append(inflated_price)
        else:
            postcodes[row[3]] = [inflated_price]

        i += 1
        if i % 100000 == 0:
            print("Completed " + str(i) + " rows")


outfile = "data/out/averagepricebypostcode.csv"
writer = csv.writer(open(outfile, "w+"))

for p in postcodes:

    avg = 0
    for val in postcodes[p]:
        avg += val

    avg = avg/len(postcodes[p])

    row = [p, avg]

    writer.writerow(row)






