from player import Player

def main():
    players = create_list("wages.rtf")
    objects = convert_to_player(players)
    # for player in objects:
    #     print(player.__str__())

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
    return player_objects

main()