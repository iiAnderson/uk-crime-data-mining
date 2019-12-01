import sys
import csv

how_to_use = "\n--------\n To Use: python3 CheckCSVForValue.py <CSV File> <Value Type (int/str)> <Row Index to Search> <Value ..> \n" \
             " Eg: Searching for a postcode python3 CheckCSVForValue.py data/ukpostcodes.csv str 3 UB10 8FZ \n --------"

fail = False
if len(sys.argv) <= 1:
    print("No CSV Specified ")
    fail = True
if len(sys.argv) <= 2:
    print("No value type specified")
    fail = True
if len(sys.argv) <= 3:
    print("No value specified")
    fail = True
if len(sys.argv) <= 4:
    print("No column index specified" + how_to_use)
    fail = True

if fail:
    sys.exit()

in_csv = sys.argv[1]
val_type = sys.argv[2]
index = int(sys.argv[3])
val = ""

for arg in sys.argv[4:]:
   val += str(arg) + " "

val = val.strip()
print("Attempting to locate + " + str(val) + " in dataset " + str(in_csv))

print("--------------")
print("Opening dataset " + in_csv)
with open(in_csv, "r") as f:
    reader = csv.reader(f)
    print("Dataset Loaded Successfully")

    value = None
    if val_type == "int":
        value = int(val)
    else:
        value = str(val)

    i = 0
    for row in reader:

        csv_val = None
        if val_type == "int":
            csv_val = int(row[index])
        else:
            csv_val = str(row[index])

        if csv_val == value:
            print("Found value " + str(value) + " in row " + str(i))

        i +=1



