"""
Глобальные переменные и условные константы.
"""

# импорты модулей стандартной библиотеки
from collections.abc import Sequence
from numbers import Real
from pathlib import Path
from re import Pattern, compile
from sys import argv, path
from typing import Any, Callable

# переменные для аннотации
Series = Sequence[Real | str]
Matrix = Sequence[Series]


DEBUG: bool = 'test' in argv
debug_data: dict[str, Any]


ROOT_DIR = Path(path[0]).parent

test_path = 'test/' if DEBUG else ''
players_path = ROOT_DIR / f'data/{test_path}players.ini'
saves_path = ROOT_DIR / f'data/{test_path}saves.txt'


players_db: dict[str, dict[str, int]] = {}
saves_db: dict[tuple[str, str], tuple[int, list[int]]] = {}


pat_player_name: Pattern = compile(r'[A-Za-zА-Яа-я]\w*')
field_pattern = compile(r'[3-9]|1\d|20') 

authorized: str = None

TOKENS: tuple[str, str] = ('X', 'O')

active_players_names: list[str] = []
active_players_funcs: list[Callable] = []
get_bot_turn: Callable = None

START_MATRICES: tuple[Matrix, Matrix] = ()

WEIGHT_OWN = 1.5
WEIGHT_FOE = 1.0

dim: int = 3
all_cells: int = dim**2
dim_range: range = range(dim)
all_cells_range: range = range(1, all_cells+1)

win_combinations: list[set[int]] = []

field_template: str = None
field_template_0: str = None

empty: dict[int, str] = {}
turns: dict[int, str] = {}

MESSAGES = {
    'ввод имени': "\n _ введите имя пользователя > ",
    'некорректное имя': " ! имя пользователя должно начинаться с буквы и далее содержать только буквы, цифры и символ '_'",
    
    'ввод команды': "\n _ введите команду > ",
    'некорректная команда': ' ! используйте команды из списка ниже',
    'колличество игроков': '\n _ какое колличество человек будет играть? Введите 1 или 2: ',
    'ввод хода': '\n _ введите номер свободной ячейки > ',
    'ход не число': ' ! номер ячейки должен быть числом',
    'ход не в диапазоне': f' ! номер ячейки должен находиться в диапазоне от 1 до {all_cells} включительно',
    'ход в занятую': ' ! ячейка занята',
    'размер поля': '\n _ Введите новый размер игрового поля в диапазоне от 3 до 20: ',
    'некорректный размер': '\n! Размер должен быть введен числом от 3 до 20 !',
    'недопустимое значение': '\n! Недопустимое значение !',
    'ничья': '\nПартия закончена. Ничья\n',
    'уровень бота': '\nВведите уровень бота (l - легкий, 2 - сложный): ',
    'ошибка команды': '\n! Недопустимая команда !\n',
}

COMMANDS = {
    'начать новую партию': ('new', 'n', 'начать', 'н'),
    'загрузить существующую партию': ('load', 'l', 'загрузка', 'з'),
    'отобразить раздел помощи': ('help', 'h', 'помощь', 'п'),
    'создать или переключиться на игрока': ('player', 'p', 'игрок', 'и'),
    'отобразить таблицу результатов': ('table', 't', 'таблица', 'т'),
    'изменить размер поля': ('dim', 'd', 'размер', 'р'),
    'выйти': ('quit', 'q', 'выход', 'в'),
}
