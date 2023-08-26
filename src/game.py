"""
Игровой процесс.
"""

# импорты модулей стандартной библиотеки
from itertools import islice
from typing import Literal
# импорты модулей проекта
import data
import player
import utils


def new() -> None:
    """"""
    


def load():
    """"""
    


def control(loaded: bool = False):
    """Управялющая функция среднего уровня."""
    # игровой процесс
    result = game()
    # партия доиграна
    if result is not None:
        player.update_stats(result)
        # удаление доигранного сохранения
        if loaded:
            data.saves_db.pop(tuple(data.active_players_names), None)
    # партия завершена досрочно
    else:
        save()
    # приведение глобальных переменных к состоянию до начала игры
    data.active_players_names = [data.authorized]
    data.active_players_names = [player.get_human_turn]
    data.turns.clear()


def game() -> tuple[str, str] | Literal[()] | None:
    """Реализация игрового процесса."""
    for turn in range(len(data.turns), data.all_cells):
        # индекс-указатель (pointer)
        p = turn % 2
        # запрос или вычисление хода
        turn = data.active_players_funcs[p]()
        # проверка на досрочное завершение партии
        if turn is None:
            return None
        # обновление словаря сделанных ходов
        data.turns |= {turn: data.TOKENS[p]}
        # вывод игрового поля в stdout
        print(utils.render_field(p))
        # проверка на наличие победной комбинации
        if check_win(p):
            return data.active_players_names[p], data.active_players_names[p-1]
    # ничья
    else:
        return ()


def check_win(pointer: int) -> bool:
    """"""
    turns = set(islice(data.turns, pointer, None, 2))
    for comb in data.win_combinations:
        if comb <= turns:
            return True
    else:
        return False


def save():
    """"""
    

