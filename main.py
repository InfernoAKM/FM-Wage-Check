import operator
from player import Player

def main():
    players = create_list("wages.rtf")
    objects = convert_to_player(players)
    wage = int(input("Enter wage budget: "))
    wage_split = wage_budget(wage)
    status_list = status_split(objects)

    print("----------\nKey Players\n----------")
    print_status(status_list, 0)
    print("----------\nFirst Team\n----------")
    print_status(status_list, 1)
    print("----------\nBackup\n----------")
    print_status(status_list, 2)


def create_list(file):
    players = []
    file_open = open(file, encoding="utf8")
    next(file_open)

    for line in file_open:
        if line.strip() and 'Wage' not in line:
            player = [line[1:-3].strip() for line in line[1:-3].split("|") if not line[1:-3].startswith("-")]
            players.append(player)

    # Removes empty lines
    players = [x for x in players if x != [] and x != ['']]
    return players

def convert_to_player(players):
    player_objects = []
    for player in players:
        player_objects.append(Player(player[0], player[1], player[2]))
    
    # Sorts by wage descending
    player_objects = sorted(player_objects, key=operator.attrgetter("wage"), reverse=True)
    return player_objects

def wage_budget(wage):
    key_player_wage = int((wage * 0.3)/4)
    first_team_wage = int((wage * 0.3)/7)
    backup_wage = int((wage * 0.3)/12)
    return (key_player_wage, first_team_wage, backup_wage)

def status_split(objects):
    key_players = []
    first_team = []
    backups = []
    for player in objects:
        if player.get_status() == "Star Player" or player.get_status() == "Important Player":
            key_players.append(player)
        elif player.get_status() == "Regular Starter" or player.get_status() == "First-Choice Goalkeeper":
            first_team.append(player)
        else:
            backups.append(player)
    return (key_players, first_team, backups)

def print_status(status_list, n):
    for player in status_list[n]:
        print(player.__str__())

main()