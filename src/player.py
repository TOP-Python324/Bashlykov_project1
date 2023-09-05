"""
Работа с данными игроков.
"""

# импорты модулей проекта
import data
import utils


def get_player_name() -> str:
    """"""
    while True:
        name = input(data.MESSAGES['ввод имени'])
        if data.pat_player_name.fullmatch(name):
            return name
        else:
            print(data.MESSAGES['некорректное имя'])


def get_player(authorize: bool = False) -> None:
    """"""
    name = get_player_name()
    if name not in data.players_db:
        data.players_db |= {
            name: {
                'побед': 0,
                'поражений': 0,
                'ничьих': 0
            }
        }
        utils.write_players(data.players_db, data.players_path)
    if authorize:
        data.authorized = name
    data.active_players_names.append(name)
    data.active_players_funcs.append(get_human_turn)
    

def get_human_turn(pointer=None) -> int | None:
    """"""
    while True:
        turn = input(data.MESSAGES['ввод хода'])
        if not turn:
            return None
        try:
            turn = int(turn)
        except ValueError:
            print(data.MESSAGES['ход не число'])
        else:
            if turn in data.all_cells_range:
                if turn not in data.turns:
                    return turn
                else:
                    print(data.MESSAGES['ход в занятую'])
            else:
                print(data.MESSAGES['ход не в диапазоне'])


def update_stats(game_result: tuple):
    """"""

