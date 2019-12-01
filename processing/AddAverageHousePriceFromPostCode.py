import csv, re

AVERAGE_PRICE_POSTCODE_FILE = "../data/averagepricebypostcode.csv"
DATA_FILE = "../data/training_set_with_postcodes.csv"
OUTPUT_FILE = "../data/training_set_with_avg_house_price.csv"

postcodes = {}

with open(AVERAGE_PRICE_POSTCODE_FILE, "r") as avg_price_postcode_file:
	reader = csv.reader(avg_price_postcode_file)

	for row in reader:
		postcodes[row[0]] = row[1]

count = 0

with open(OUTPUT_FILE,"w+") as output:
	with open(DATA_FILE,"r") as data:
		reader = csv.reader(data)
		writer = csv.writer(output)

		def addRow(row,postcode):
			newrow = row
			if postcode in postcodes:
				newrow.append(postcodes[postcode])
			else:
				newrow.append("")

			writer.writerow(newrow)

		for row in reader:
			row[5] = re.sub(' +',' ',row[5])
			row[6] = re.sub(' +',' ',row[6])

			if " " in row[5]:
				addRow(row,row[5])
			elif " " in row[6]:
				addRow(row,row[6])
			else:
				print "Error"
				print row
				count = count+1

print count