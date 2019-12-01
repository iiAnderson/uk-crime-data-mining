import csv

# Population counts by age and sex

infile = "../MYEB1_detailed_population_estimates_series_UK_(0116).csv"
outfile = "../population_by_age_and_sex.csv"
writer = csv.writer(open(outfile, "w+", newline=""))

with open(infile, "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:
        out_row = []

        # lad2014info, country, sex and age
        out_row += row[0:5]

        # population for the years 2014-2016
        out_row += row[18:21]

        writer.writerow(out_row)

        i += 1
        if i % 100000 == 0:
            print("Processed " + str(i) + " rows")
    print("Population by Sex and Age Dataset Loaded successfully")

# Population counts by age and sex

infile = "../MYEB3_summary_components_of_change_series_UK_(0216).csv"
outfile = "../population_changes.csv"
writer = csv.writer(open(outfile, "w+", newline=""))

with open(infile, "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:
        out_row = []

        # lad2014info and country
        out_row += row[0:5]

        # births, deaths, change due to natural causes, moving within and outside of the country,
        #  other change and population counts for the years 2014-2016
        out_row += row[136:169]

        writer.writerow(out_row)

        i += 1
        if i % 100000 == 0:
            print("Processed " + str(i) + " rows")
    print("Population Change Dataset Loaded successfully")

