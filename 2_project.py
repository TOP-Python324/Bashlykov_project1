def winning_combinations(cell: int) -> list[set]:
    """Генерирует и возвращает список множеств выигрышных комбинаций"""
    list_of_sets = []
    #горизонтальные комбинации
    for i in range(1, cell**2 + 1, cell):
        list_of_sets += [set(range(i, i+cell))]
    # вертикальные комбинации
    for i in range(1, cell + 1):
        list_of_sets += [set(range(i, cell**2 + 1, cell))]
    #диагональные комбинации
    list_of_sets += [set(range(1, cell**2 + 1, cell+1))]
    list_of_sets += [set(range(cell, cell**2-1, cell - 1))]
    return list_of_sets

# >>> winning_combinations(4)
# [{1, 2, 3, 4}, {8, 5, 6, 7}, {9, 10, 11, 12}, {16, 13, 14, 15}, {1, 13, 5, 9}, {2, 10, 6, 14}, {11, 3, 15, 7}, {8, 16, 4, 12}, {16, 1, 11, 6}, {10, 4, 13, 7}]