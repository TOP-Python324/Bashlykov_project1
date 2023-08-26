from configparser import ConfigParser
from pathlib import Path
from sys import path


script_dir = Path(path[0])
test_players_path = script_dir / 'test_players.ini'
test_saves_path = script_dir / 'test_saves.txt'


players = ConfigParser()
players.read(test_players_path)

# {
#   'имя_игрока_1': { 'побед': 5,
#                     'поражений': 3,
#                     'ничьих': 10    },
#   'имя_игрока_2': { 'побед': 0,
#                     'поражений': 0,
#                     'ничьих': 0     },
#   ...,
# }
    
players_db = {
    name: {
        key: int(val)
        for key, val in players[name].items()
    }
    for name in players.sections()
}


# {
#   ('имя_игрока_1', 'имя_игрока_2'): (3, [5, 3, 9]),
#   ('имя_игрока_2', 'имя_игрока_1'): (3, [1, 9, 5, 3]),
#   ...,
# }

with open(test_saves_path, encoding='utf-8') as test_saves:
    saves = test_saves.read().split()

saves_db = {}
for line in saves:
    players, dim, turns = line.split('!')
    players = tuple(players.split(','))
    dim = int(dim)
    turns = [int(t) for t in turns.split(',')]
    saves_db |= {players: (dim, turns)}

