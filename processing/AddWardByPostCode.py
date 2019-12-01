import csv, re

POSTCODE_WARD_FILE = "../data/pcd11_par11_wd11_lad11_ew_lu.csv"
POPULATION_ESTIMATES_MALE = "../data/mid-2016-males.csv"
POPULATION_ESTIMATES_FEMALE = "../data/mid-2016-females.csv"

DATA_FILE = "../data/training_set_houseprice_population_deprivation.csv"
OUTPUT_FILE = "../data/training_set_houseprice_population_deprivation_clean.csv"

postcodes = {}
male_population = {}
female_population = {}

with open(POSTCODE_WARD_FILE, "r") as postcode_ward_file:
	reader = csv.reader(postcode_ward_file)

	for row in reader:
		postcodes[row[2]] = row[6]

with open(POPULATION_ESTIMATES_MALE, "r") as f:
	reader = csv.reader(f)
	reader.next()

	for row in reader:
		male_population[row[0]] = row[3:]
		male_population[row[0]][0] = male_population[row[0]][0].replace(",","")

with open(POPULATION_ESTIMATES_FEMALE, "r") as f:
	reader = csv.reader(f)
	reader.next()

	for row in reader:
		female_population[row[0]] = row[3:]
		female_population[row[0]][0] = female_population[row[0]][0].replace(",","")

count = 0

writer = csv.writer(open(OUTPUT_FILE,"w+"))
with open(DATA_FILE,"r") as data:
	reader = csv.reader(data)

	def addRow(row,postcode):
		newrow = [row[0].split("-")[0],row[0].split("-")[1]] #Split date/month
		for i in range(1,len(row)):
				newrow.append(row[i])
		# success = True

		#newrow = row
		del newrow[7]
		newrow[6] = postcode		
		newrow.append(postcodes[postcode])
		if postcodes[postcode] in male_population:
			newrow.extend(male_population[postcodes[postcode]])
			newrow.extend(female_population[postcodes[postcode]])
			writer.writerow(newrow)
			return True
		else:
			return False

		# if postcode in postcodes:
		# 	newrow.append(postcodes[postcode])
		# else:
		# 	newrow.append("")

		# writer.writerow(newrow)
		# return success

	for row in reader:
		row[6] = re.sub(' +',' ',row[6])
		row[7] = re.sub(' +',' ',row[7])

		if " " in row[6]:
			if not addRow(row,row[6]):
				count = count+1
		elif " " in row[7]:
			if not addRow(row,row[7]):
				count = count+1
		else:
			print "Error"
			print row
			count = count+1

print count