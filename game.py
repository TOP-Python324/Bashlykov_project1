from itertools import islice
from re import compile

#Шаблон (регулярное выражение) для имени игрока
name_pattern = compile(r'[A-Za-zА-Яа-я]\w*') 

def name_input() -> str:
    """Запрашивает у пользователя и возвращает его имя"""
    while True:
        name_str = input("Введите свое имя: ")
        if name_pattern.fullmatch(name_str):
            return name_str
        print(f"размер игрового поля в диапазоне от 3 до 20")
    
name_str = name_input()

#Шаблон (регулярное выражение) для размера игрового поля
field_pattern = compile(r'[3-9]|1\d|20') 

def cell_input() -> int:
    """Запрашивает у пользователя и возвращает размер поля"""
    while True:
        cell_str = input("Введите колличество клеток: ")
        if field_pattern.fullmatch(cell_str):
            return int(cell_str)
        print(f"Число введено неверно. Введите число соответствующее правилам игры")
    
cell_str = cell_input()
cell = int(cell_str)
    
def generator_field(cell: int) -> str:
    """Генерирует шаблон игрового поля соответствующего размера, для отображения"""
    row = '|'.join([' {} ']*cell)
    line = '-'*(cell*3 + (cell-1))
    return (f'\n{line}\n'.join([row]*cell))
    
empty_dict = dict.fromkeys(range(1, cell**2 + 1), ' ')
#turns = {5: 'X', 9: '0', 3: 'X', 1: '0', 2:'X', 6: '0', 7: 'X', 4: '0'}
turns = {5: 'X', 9: '0', 4: 'X', 1: '0', 2:'X', 6: '0', 7: 'X', 3: '0'}
#turns = {4: 'X', 9: '0', 3: 'X', 1: '0', 5: 'X', 7: '0', 2: 'X'}
board = generator_field(cell).format(*(empty_dict | turns).values())

def winning_combinations(cell: int) -> list[set]:
    """Генерирует и возвращает список множеств выигрышных комбинаций"""
    list_of_sets = []
    # горизонтальные комбинации
    for i in range(1, cell**2 + 1, cell):
        list_of_sets += [set(range(i, i+cell))]
    #вертикальные комбинации
    for i in range(1, cell + 1):
        list_of_sets += [set(range(i, cell**2 + 1, cell))]
    #диагональные комбинации
    list_of_sets += [set(range(1, cell**2 + 1, cell+1))]
    list_of_sets += [set(range(cell, cell**2-1, cell - 1))]
    return list_of_sets

def check_combination(winning_combinations: list[set]) -> None:
    """Проверяет сделанные ходы с выигрышными комбинациями"""
    crosses = set(islice(turns, 0, None, 2))
    zeros = set(islice(turns, 1, None, 2))
    
    for comb in winning_combinations:
        if comb <= crosses:
            print(f"Crosses is winner!")
            break
        if comb <= zeros:
            print(f"Zeros is winner!")
            break
    return None

# > python -i game.py
# Введите свое имя: про 1
# Имя введено неверно. Введите имя соответствующее правилам игры
# Введите свое имя: Александр
# Введите колличество клеток: 21
# размер игрового поля в диапазоне от 3 до 20
# Введите колличество клеток: 3
# >>> winning_combinations(3)
# [{1, 2, 3}, {4, 5, 6}, {8, 9, 7}, {1, 4, 7}, {8, 2, 5}, {9, 3, 6}, {1, 5, 9}, {3, 5, 7}]
# >>> print(board)
 # 0 | X | 0
# -----------
 # X | X | 0
# -----------
 # X |   | 0
# >>> check_combination(winning_combinations(3))
# Zeros is winner!

# > python -i game.py
# Введите колличество клеток: 3
# >>> print(board)
 # 0 | X | X
# -----------
 # 0 | X | 0
# -----------
 # X |   | 0
# >>> check_combination(winning_combinations(3))
# Crosses is winner!