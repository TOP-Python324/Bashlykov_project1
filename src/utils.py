"""
Вспомогательные функции.
"""

# импорты модулей стандартной библиотеки
from configparser import ConfigParser
from pathlib import Path
from pprint import pprint
from shutil import get_terminal_size
from typing import Literal
# импорты модулей проекта
import data


def read_players(filein_path: Path, buffer: dict) -> None:
    """"""
    players_data = ConfigParser()
    players_data.read(filein_path)
    buffer |= {
        player: {
            k: int(v) 
            for k, v in players_data[player].items()
        }
        for player in players_data.sections()
    }


def read_saves(filein_path: Path, buffer: dict) -> None:
    """"""
    try:
        saves_data = filein_path.read_text(encoding='utf-8').split('\n')
    except FileNotFoundError:
        pass
    else:
        for line in saves_data:
            try:
                players, dim, turns = line.split('!')
            except ValueError:
                return
            players = tuple(players.split(','))
            dim = int(dim)
            turns = [int(t) for t in turns.split(',')]
            buffer |= {players: (dim, turns)}


def write_players(buffer: dict, fileout_path: Path) -> None:
    """"""
    players_data = ConfigParser()
    players_data.read_dict(buffer)
    with open(fileout_path, 'w', encoding='utf-8') as fileout:
        players_data.write(fileout)


def write_saves(buffer: dict, fileout_path: Path) -> None:
    """"""
    players_data = []
    for players, turns in buffer.items():
        dim, turns = turns
        players = ','.join(players)
        turns = ','.join(str(t) for t in turns)
        players_data.append('!'.join((players, str(dim), turns)))
    with open(fileout_path, 'w', encoding='utf-8') as fileout:
        fileout.write('\n'.join(players_data))


def change_dim(new_dim: int) -> None:
    """"""
    data.dim = new_dim
    data.all_cells = new_dim**2
    data.dim_range = range(new_dim)
    data.all_cells_range = range(1, data.all_cells+1)
    data.win_combinations = generate_win_combinations(new_dim)
    data.field = generate_field_template(new_dim)
    data.empty = dict.fromkeys(data.all_cells_range, ' ')


def header_text(
        text: str,
        *,
        level: Literal[1, 2],
        v_fill: str = '#',
        h_fill: str = '='
) -> str:
    """Возвращает переданную строку, форматированную как заголовок. Форматирование отличается для разных уровней заголовка. Также могут быть изменены символы-заполнители."""
    term_width = get_terminal_size()[0] - 1
    data_width = term_width - 12
    text_len = len(text)

    if level == 1:
        text = text.upper()
        edge = v_fill + h_fill*(term_width-2) + v_fill
        padding = v_fill + ' '*(term_width-2) + v_fill
        text = '\n'.join(
            v_fill + line.center(term_width - 2) + v_fill
            for line in columnize(text, term_width - 6)
        )
        return f'{edge}\n{padding}\n{text}\n{padding}\n{edge}'

    elif level == 2:
        text = text.upper()
        if text_len <= data_width:
            return f'  {text}  '.center(term_width, h_fill)
        else:
            return '\n'.join(
                h_fill*4 + line.center(data_width + 4) + h_fill*4
                for line in columnize(text, data_width)
            )

    # можно добавить дополнительные уровни заголовков с собственным форматированием
    # elif level == 3:
    #     ...

    else:
        raise ValueError


def columnize(text: str, column_width: int) -> list[str]:
    """Разбивает переданную строку на отдельные слова и формирует из слов строки, длины которых не превышают заданное значение. Возвращает список строк, к которым впоследствии может быть применено любое выравнивание."""
    multiline, line_len, i = [[]], 0, 0
    for word in text.split():
        word_len = len(word)
        if line_len + word_len + len(multiline[i]) <= column_width:
            multiline[i] += [word]
            line_len += word_len
        else:
            multiline += [[word]]
            line_len = word_len
            i += 1
    return [' '.join(line) for line in multiline]


def generate_win_combinations(new_dim: int) -> list[set[int]]:
    """"""
    


def generate_field_template(new_dim: int) -> str:
    """"""
    


def render_field(pointer: int) -> str:
    """"""
    if pointer:
        # вывод поля крестика (слева)
        data.field.format(*(data.empty | data.turns).values())
    else:
        # вывод поля нолика (справа)
        ...
