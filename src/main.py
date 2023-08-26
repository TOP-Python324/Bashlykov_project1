"""
Точка входа — основной управляющий код.
"""

# импорты модулей проекта
import data
import help
import game
import player
import utils


def start():
    """Инициализация приложения.
    
    Управялющая функция верхнего уровня."""
    utils.read_players(data.players_path, data.players_db)
    utils.read_saves(data.saves_path, data.saves_db)
    
    if data.players_db:
        print(help.render_commands())
    else:
        ...
        # help.show_full()
    
    player.get_player(True)
    utils.change_dim(3)


def main_menu():
    """Суперцикл главного меню.
    
    Управялющая функция верхнего уровня."""
    while True:
        command = input(data.MESSAGES['ввод команды'])
        
        if command in data.COMMANDS['начать новую партию']:
            # настройка новой партии
            game.new()
            # передача управления на средний уровень
            game.control()
        
        elif command in data.COMMANDS['загрузить существующую партию']:
            # загрузка существующей партии
            game.load()
            # передача управления на средний уровень
            game.control(loaded = True)
        
        # elif command in data.COMMANDS['']:
        
        elif command in data.COMMANDS['выйти']:
            break
        
        else:
            print(help.render_commands(header=False))


def end():
    """Завершение работы приложения.
    
    Управялющая функция верхнего уровня."""
    


if __name__ == '__main__':
    start()
    main_menu()
    end()

