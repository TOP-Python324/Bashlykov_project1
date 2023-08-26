def easy():
    """Вычисляет ход лёгкого бота"""
    print('ход лёгкого бота')


def hard():
    """Вычисляет ход сложного бота"""
    print('ход сложного бота')


def get_human_turn():
    """Запрашивает ход человека"""
    print('ход человека')



active_players = {}
TOKENS = ('X', 'O')

# 3. ... внести имя игрока в словарь активных игроков
active_players['авторизованный_игрок'] = get_human_turn

# 5. ... добавить имя бота объект функции хода бота в зависимости от уровня сложности в словарь активных игроков
active_players['#1'] = easy

# 5. ... запросить очерёдность ходов
# авторизованный_игрок выбирает нолик
active_players = dict(reversed(active_players.items()))

for turn in range(9):
    # индекс-указатель
    o = turn % 2
    # print(f'{turn=} {o=}')
    print(TOKENS[o], tuple(active_players.keys())[o], end=' ')
    tuple(active_players.values())[o]()



# 3. ... внести имя игрока в список имён активных игроков и объект функции запроса хода человека в список функций активных игроков
active_players_names = ['авторизованный_игрок']
active_players_funcs = [get_human_turn]

# 5. ... добавить имя бота в список имён активных игроков и объект функции хода бота в зависимости от уровня сложности в список функций активных игроков
active_players_names += ['#1']
active_players_funcs += [easy]

# 5. ... запросить очерёдность ходов
# авторизованный_игрок выбирает нолик
active_players_names.reverse()
active_players_funcs.reverse()

turns: dict[int, str] = {}

for turn in range(9):
    # индекс-указатель
    o = turn % 2
    # print(f'{turn=} {o=}')
    # print(active_players_names[o])
    # turn = active_players_funcs[o]()
    turns |= {turn: TOKENS[o]}


# >>> names = ['a', 'b']
# >>>
# >>> p = 0
# >>> names[p]
# 'a'
# >>> names[p-1]
# 'b'
# >>>
# >>> p = 1
# >>> names[p]
# 'b'
# >>> names[p-1]
# 'a'