import csv

player_list = []
experienced_players = []
inexperienced_players = []
raptors = []
sharks = []
dragons = []
my_teams = {}

# Open file
def open_mycsv():
    with open('/Users/kirstenschwarzer/Code/treehouse-project-1/soccer_players.csv', 'r') as csvfile:
        playerreader = csv.reader(csvfile)
        for row in playerreader:
            player_list.append(row)
        csvfile.close()

# Sort players by experience
def experience(player_list, experienced_players, inexperienced_players):
    for row in player_list:
        for attribute in row:
            if 'YES' in attribute:
                experienced_players.append(row)
            if 'NO' in attribute:
                inexperienced_players.append(row)

# Divide players into teams and write to teams.txt file
def divide_teams(experienced_players, inexperienced_players):
    raptors = experienced_players[::3] + inexperienced_players[::3]
    sharks = experienced_players[1::3] + inexperienced_players[1::3]
    dragons = experienced_players[2::3] + inexperienced_players[2::3]

    my_teams = {"Raptors": raptors, "Sharks": sharks, "Dragons": dragons}

    # Create output teams.txt file
    with open("/Users/kirstenschwarzer/Code/treehouse-project-1/teams.txt", "a") as teamfile:
        for name, players in my_teams.items():
            teamfile.write(name + "\n")
            for player in players:
                teamfile.write(', '.join(player) + "\n")
            teamfile.write("\n")

    teamfile.close()

if __name__ == '__main__':
    open_mycsv()
    experience(player_list, experienced_players, inexperienced_players)
    divide_teams(experienced_players, inexperienced_players)
