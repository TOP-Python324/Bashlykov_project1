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
    
    Управляющая функция верхнего уровня."""
    utils.read_players(data.players_path, data.players_db)
    utils.read_saves(data.saves_path, data.saves_db)
    
    if data.players_db:
        # ИСПРАВИТЬ: заголовок игры необходимо выводить в любом случае
        print(help.game_title())
    else:
        print(help.render_commands())
        # help.show_full()
    
    player.get_player(True)
    # ИСПРАВИТЬ: перенесите этот код выше, сразу после чтения файлов
    utils.change_dim(3)


def main_menu():
    """Суперцикл главного меню.
    
    Управляющая функция верхнего уровня."""
    while True:
        command = input(data.MESSAGES['ввод команды'])
        
        if command in data.COMMANDS['начать новую партию']:
            # настройка новой партии
            game.new()
            # выводим координатную сетку перед первым ходом
            # ИСПРАВИТЬ: используйте уже созданный с помощью utils.change_dim() шаблон, а не генерируйте новый
            # УДАЛИТЬ: вынесите этот код в отдельную функцию в модуль help
            print(utils.generate_field_template().format(*(data.empty.keys())))
            # передача управления на средний уровень
            game.control()
        
        elif command in data.COMMANDS['загрузить существующую партию']:
            # загрузка существующей партии
            game.load()
            # передача управления на средний уровень
            game.control(loaded=True)
        
        elif command in data.COMMANDS['отобразить раздел помощи']:
            print(help.render_commands())

        elif command in data.COMMANDS['создать или переключиться на игрока']:
            ...

        elif command in data.COMMANDS['отобразить таблицу результатов']:
            ...

        elif command in data.COMMANDS['изменить размер поля']:
            utils.change_dim(utils.dim_input())
            

        elif command in data.COMMANDS['выйти']:
            break
        
        else:
            print(help.render_commands(header=False))


def end():
    """Завершение работы приложения.
    
    Управляющая функция верхнего уровня."""



if __name__ == '__main__':
    start()
    main_menu()
    end()

