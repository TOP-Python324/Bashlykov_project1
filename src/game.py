"""
Игровой процесс.
"""

# импорты модулей стандартной библиотеки
from itertools import islice
from typing import Literal
# импорты модулей проекта
import bot
import data
import player
import utils


def new() -> None:
    """Определяет режим игры"""
    # ИСПРАВИТЬ: перепишите функцию так, чтобы в своём условно-бесконечном цикле был каждый отдельный запрос, а не все разом в одном цикле
    while True:
        num_people = int(input(data.MESSAGES['количество игроков']))
        # если два игрока
        if num_people == 2:
            # Запрос имени второго игрока
            player.get_player()
            # ДОБАВИТЬ: объект функции player.get_human_turn в active_players_funcs
            break
        # если один игрок то запрашиваем уровень бота
        elif num_people == 1:    
            bot_level = input(data.MESSAGES['уровень бота'])
            # ИСПРАВИТЬ: бесконечный цикл
            while bot_level != '1' and bot_level != '2':
                print(data.MESSAGES['недопустимое значение'])
                bot_level = input(data.MESSAGES['уровень бота'])
                
            if bot_level == '1':
                data.active_players_names += ["#1"]
                # ИСПРАВИТЬ: не в data.get_bot_turn, такой переменной вообще не должно быть
                data.get_bot_turn = bot.easy_mode
            else:
                data.active_players_names += ["#2"]   
                data.get_bot_turn = bot.hard_mode    
            break
        else:
            print(data.MESSAGES['недопустимое значение'])
    
    while True: 
        token = input(f'\n _ ведите токен которым будет играть {data.active_players_names[0]} (X или O): ').upper()  
        if token in ['X', '0', 'Х', '0']:
            if token == data.TOKENS[1]:
                # ИСПОЛЬЗОВАТЬ: поменять местами список из двух элементов можно и проще
                data.active_players_names = data.active_players_names[::-1]
            break
        else:
            print(data.MESSAGES['недопустимое значение']) 
            

def load():
    """"""
    


def control(loaded: bool = False):
    """Управляющая функция среднего уровня."""
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
    # УДАЛИТЬ: вот и ответ, отчего у вас размер поля не меняется: вы меняете его через команду, а потом здесь переопределяете часть переменных
    # КОММЕНТАРИЙ: а ведь мы говорили, что специально выносим весь код по переопределению глобальных переменных в utils.change_dim()
    # Инициализация перед началом партии
    data.win_combinations = utils.generate_win_combinations()
    data.field_template = utils.generate_field_template()
    data.field_template_0 = utils.generate_field_template_0()
    data.empty = dict.fromkeys(range(1, data.all_cells+1), ' ')
    
    #  Цикл до максимального количества ходов
    for turn in range(len(data.turns), data.all_cells):
        # индекс-указатель (pointer)
        p = turn % 2
        # запрос или вычисление хода
        # ИСПРАВИТЬ: в переменной data.active_players_funcs
        # turn = data.active_players_funcs[player.get_human_turn()](p)
        turn = player.get_human_turn()
        # проверка на досрочное завершение партии
        if turn is None:
            return None
        # обновление словаря сделанных ходов
        data.turns |= {turn: data.TOKENS[p]}
        # вывод игрового поля в stdout
        # ИСПРАВИТЬ: пишите отдельную функцию, отлаживайте её отдельно, а затем интегрируйте в проект
        # print(utils.render_field(p))
        # УДАЛИТЬ: не нужно вот такого полу-временного/полу-постоянного кода — это сильно ухудшает ориентирование в проекте
        # print(data.field_template.format(*(data.empty | data.turns).values()))
        if p:
            # вывод поля нолика (справа)
            print(data.field_template_0.format(*(data.empty | data.turns).values()))
        else:
            # вывод поля крестика (слева)
            print(data.field_template.format(*(data.empty | data.turns).values()))
        # УДАЛИТЬ: аналогично
        # проверка на наличие победной комбинации
        turns = set(islice(data.turns, p, None, 2))
        for comb in data.win_combinations:
            if comb <= turns:
                print(f'\nВыиграл {data.active_players_names[p]}\n')
                return [data.active_players_names[p],data.active_players_names[1-p]]
    print(data.MESSAGES['ничья'])    
    return []

        # if check_win(p):
            # return data.active_players_names[p], data.active_players_names[p-1]
    # ничья
    # else:
        # return ()


# def check_win(pointer: int) -> bool:
    # """"""
    # turns = set(islice(data.turns, pointer, None, 2))
    # for comb in data.win_combinations:
        # if comb <= turns:
            # return True
    # else:
        # return False


def save():
    """"""
    

