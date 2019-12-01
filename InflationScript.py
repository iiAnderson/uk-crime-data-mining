import csv
from dateutil.parser import parse

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
    1995 : 1.0296
}


def recursive_inflation (year):
    if year == 2017:
        return yearly_inflation_rates[2017]
    else:
        return yearly_inflation_rates[year] * recursive_inflation(year-1)

infile = open('pp-2017.csv', 'rb')
reader = csv.reader(infile)
data_list = list(reader)


with open('outfile.csv', 'w') as out:
    writer = csv.writer(out)
    for f in data_list:
        date = parse(f[2])
        year = int(date.year)
        inflated_price = int(f[1])*recursive_inflation(year)
        out.write(str(date) + "," + str(f[1]) + "," + str(inflated_price)+'\n')





