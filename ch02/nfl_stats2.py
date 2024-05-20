"""
open the csv file called "nfl_offensive_stats.csv" and
read in the csv data from the file
"""

import csv

# open the csv file
with open("nfl_offensive_stats.csv", "r") as f:
    # read in the csv data
    reader = csv.reader(f)
    nfl_data = list(reader)

"""
the 3rd column in data is player position, the fourth column
is the player, and the 8th column is the passing yards.
For each player whose position in column 3 is "QB",
determine the sum of yards from column 8
"""
# create a dictionary to hold the player name and passing yards
player_passing_yards = {}

# loop through the data
for row in nfl_data:
    # check if the player's position is "QB"
    if row[2] == "QB":
        # check if the player is already in the dictionary
        if row[3] in player_passing_yards:
            # if the player is already in the dictionary, add the
            # player's passing yards to the existing value
            player_passing_yards[row[3]] += int(row[7])
        else:
            # if the player is not already in the dictionary, add
            # the player to the dictionary with the player's passing
            # yards as the value
            player_passing_yards[row[3]] = int(row[7])

"""
print the sum of the passing yards sorted by sum
of passing yards in descending order
"""
for player in sorted(player_passing_yards, key=player_passing_yards.get, reverse=True):
    print(player, player_passing_yards[player])


"""
print the sum of the passing yards sorted by sum
of passing yards in descending order
Do not include Tom Brady because he wins too much
"""
for player in sorted(player_passing_yards, key=player_passing_yards.get, reverse=True):
    if player != "Tom Brady":
        print(player, player_passing_yards[player])

"""
plot the players by their number of passing yards only for
players with more than 4000 passing yards
"""
import matplotlib.pyplot as plt
import numpy as np

# create a list to hold the players with more than 4000 passing yards
players = []
# create a list to hold the passing yards for the players with more than 4000 passing yards
passing_yards = []

# loop through the dictionary
for player in player_passing_yards:
    # check if the player has more than 4000 passing yards
    if player_passing_yards[player] > 4000:
        # if the player has more than 4000 passing yards, add the player to the players list
        players.append(player)
        # if the player has more than 4000 passing yards, add the passing yards to the passing_yards list
        passing_yards.append(player_passing_yards[player])

# create a bar chart
x = np.arange(len(players))
plt.bar(x, passing_yards)
plt.xticks(x, players, rotation=90)
plt.show()
