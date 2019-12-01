import requests
import csv

infile = "../google_maps_api_key.csv"

with open(infile, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        key = row[0]

infile = "../population_by_age_and_sex.csv"
outfile = "../population_by_age_and_sex_latlng.csv"
writer = csv.writer(open(outfile, "w+", newline=""))

lad2014names = {}
lad2014nameswithlocation = {}

with open(infile, "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    headings = []
    i = 0
    for row in reader:
        if i > 0:
            lad2014names[row[1]] = ""
        else:
            headings = row
        i += 1

    for name in lad2014names:
        # Make sure we are searching locations in the UK
        name_with_uk = name + ", UK"
        base = "https://maps.googleapis.com/maps/api/geocode/json?"
        params = "address={address}&key={key}".format(
            address=name_with_uk,
            key=key
        )
        url = "{base}{params}".format(base=base, params=params)
        response = requests.get(url)

        # The below didn't work because Google Maps API likes to lie

        # if (response.json()["results"][0]["address_components"][-1]["long_name"] != "United Kingdom" or
        #     response.json()["results"][0]["address_components"][-1]["short_name"] != "GB"):
        #     print("Problem, the location " + name + " was not found to be in the UK!")
        lad2014nameswithlocation[name] = response.json()["results"][0]["geometry"]["location"]

# Add headings (including those we are adding like lat and lng)
headings += ["lat", "lng"]
writer.writerow(headings)

with open(infile, "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:
        if i > 0:
            if lad2014nameswithlocation[row[1]]:
                row += [str(lad2014nameswithlocation[row[1]]["lat"])]
                row += [str(lad2014nameswithlocation[row[1]]["lng"])]
            writer.writerow(row)
        i += 1

infile = "../population_changes.csv"
outfile = "../population_changes_latlng.csv"
writer = csv.writer(open(outfile, "w+", newline=""))

with open(infile, "r") as f:
    reader = csv.reader(f)
    print("Success: Dataset Loaded")

    i = 0
    for row in reader:
        if i > 0:
            if lad2014nameswithlocation[row[1]]:
                row += [str(lad2014nameswithlocation[row[1]]["lat"])]
                row += [str(lad2014nameswithlocation[row[1]]["lng"])]
            writer.writerow(row)
        else:
            headings = row + ["lat", "lng"]
            writer.writerow(headings)
        i += 1
