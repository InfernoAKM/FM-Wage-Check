from player import Player

def main():
    players = create_list("wages.txt")
    convert_to_player(players)

def create_list(file):
    players = []
    file_open = open(file, encoding="utf8")
    next(file_open)

    for line in file_open:
        players.append([line[1:-3].strip() for line in line[1:-3].split("|") if not line[1:-3].startswith("-")])

    # Removes empty lines
    players = [x for x in players if x != [] and x != ['']]
    return players

def convert_to_player(players):
    player_objects = []
    for player in players:
        player_objects.append(Player(player[0], player[1], player[2]))
    # for x in player_objects:
    #     print(x.__str__())
    return player_objects

main()