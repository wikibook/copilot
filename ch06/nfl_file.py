nfl_file = open("nfl_offensive_stats.csv")
total_yards = 0
for line in nfl_file:
    lst = line.split(",")
    if lst[3] == "Aaron Rodgers":
        total_yards += int(lst[7])
nfl_file.close()
print(total_yards)

import csv

with open("nfl_offensive_stats.csv", "r") as f:
    reader = csv.reader(f)
    nfl_data = list(reader)
passing_yards = 0
for row in nfl_data:
    if row[3] == "Aaron Rodgers":
        passing_yards += int(row[7])
print(passing_yards)
