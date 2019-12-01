from glob import glob
import os
import csv
import sys

print("---------------------------")
def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

if len(sys.argv) <= 1:
    print("You must add a directory for the file, for example in windows python3 MergeCrimeData.py g:/Downloads/policedata\n"
          "This should be the root directory of the download, with all of the month dates inside this directory.")
    print("---------------------------")

location =  os.path.normpath(sys.argv[1])
out = "14-15Crime.csv"
writer = csv.writer(open(out, "w", newline=""))

folders = glob(location + "/*/")
print("Located " + str(len(folders)) + "subdirectories in the directory " + location)

rows_to_add = [1, 4, 5, 9]
i = 0
for f in folders:
    print("Beginning processing directory " + str(f))
    list = find_csv_filenames(f)

    for file in list:
        with open(f + file, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                new_row = []
                for r in rows_to_add:
                    new_row.append(row[r].replace("\r","").replace("\n",""))

                writer.writerow(new_row)
                i += 1

        print("    Processed file " + str(file))
    print("Completed Processing directory " + str(f))

print("Successfully processed "+str(i)+", output in file " + str(out))
print("---------------------------")


