import csv
from collections import Counter


accident_counter = Counter()

with open("Crimes.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row['Date'][6:10] == "2015":
            accident_counter[row['Primary Type']] += 1

print(accident_counter.most_common(1))

