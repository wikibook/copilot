"""
open the csv file called "nfl_offensive_stats.csv" and read in
the csv data from the file
"""

import csv

with open("nfl_offensive_stats.csv", "r") as f:
    reader = csv.reader(f)
    nfl_data = list(reader)

"""
In the data we just read in, the fourth column is the player
and the 8th column is the passing yards. Get the sum of
yards from column 8 where the 4th column value is
"Aaron Rodgers"
"""
passing_yards = 0
for row in nfl_data:
    if row[3] == "Aaron Rodgers":
        passing_yards += int(row[7])
print(passing_yards)
