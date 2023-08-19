from configparser import ConfigParser
from pathlib import Path
from sys import path

script_dir = Path(path[0])
players_path = script_dir / 'players.ini'
players_path1 = script_dir / 'players1.ini'
saves_path = script_dir / 'saves.txt'
saves_path1 = script_dir / 'saves1.txt'

def read_players() -> dict:
    """Читает данные из файла INI, проверяет пустой ли файл (возвращает False) и формирует базу игроков согласно структуры данных"""    
    players = ConfigParser()
    players.read(players_path, encoding='utf-8')
    players_db = {
        name: {
            key: int(val)
            for key, val in players[name].items()
        }
        for name in players.sections()
    }
    return bool(players_db), players_db
    
# >>> read_players()
# (True, {'тестовый_игрок_1': {'побед': 5, 'поражений': 3, 'ничьих': 10}, 'Тестовый_Игрок_2': {'побед': 0, 'поражений': 0, 'ничьих': 0}})

# Пустой файл
# >>> read_players()
# (False, {})

players_db = {
          'имя_игрока_1': { 'побед': 5,
                            'поражений': 3,
                            'ничьих': 10    },
          'имя_игрока_2': { 'побед': 0,
                            'поражений': 0,
                            'ничьих': 0     }
            }

def write_players() -> None:
    """Записывает в файл данные игроков (имя, победы, поражения, ничьи) из даныых игры."""
    players = ConfigParser()
    players.read_dict(players_db)
    with open(players_path1, "w", encoding="utf-8") as file_out:
         players.write(file_out)
    return None

# >>> write_players()
# >>>
#Создался новый файл players1.ini

def read_saves() -> dict:
    """Читает данные из файла txt сохранённых партий, проверяет пустой ли файл (возвращает False) и формирует базу схраненных партий согласно структуры данных"""
    with open(saves_path, encoding='utf-8') as game_saves:
        saves = game_saves.read().split()
    saves_db = {}
    for line in saves:
        players, cell, turns = line.split('!')
        players = tuple(players.split(','))
        cell = int(cell)
        turns = [int(t) for t in turns.split(',')]
        saves_db |= {players: (cell, turns)}
    return bool(saves_db), saves_db    
    
# >>> read_saves()
# (True, {('имя_игрока_1', 'имя_игрока_2'): (3, [5, 3, 9]), ('имя_игрока_2', 'имя_игрока_1'): (3, [1, 9, 5, 3]), ('имя_игрока_3', 'имя_игрока_1'): (5, [12, 0, 7, 1, 17, 20])})

#читает пустой файл
# >>> read_saves()
# (False, {})

saves_db = {('имя_игрока_1', 'имя_игрока_2'): (3, [5, 3, 9]), 
('имя_игрока_2', 'имя_игрока_1'): (3, [1, 9, 5, 3])}

def write_saves() -> None:
    """Записывает в файл сохранённых партий из даныых игры."""
    with open(saves_path1, encoding='utf-8') as game_saves:
        saves1 = game_saves.write(str1)
        st = ' '.join(f"{k}!{v}" for k,v in saves_db.items())
        str1 = st.replace('(', '').replace(')', '').replace("'", '')