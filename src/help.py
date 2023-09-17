"""
Раздел помощи.
"""

# импорты модулей стандартной библиотеки
from shutil import get_terminal_size
# импорты модулей проекта
import data
import utils


def render_commands(header: bool = True) -> str:
    """Возвращает строку с подзаголовком (опционально) и подразделом справки о командах главного меню.

    :param header: добавить или не добавлять подзаголовок
    """
    if header:
        commands = f'\n{utils.header_text("команды", level=2)}\n\n'
    else:
        commands = f"{data.MESSAGES['некорректная команда']}\n\n"
    widths = [max(len(option) for option in column) for column in zip(*data.COMMANDS.values())]
    for command, options in data.COMMANDS.items():
        options = ' : '.join(f'{o:<{widths[i]}}' for i, o in enumerate(options))
        commands += f'{command} : {options} :'.rjust(get_terminal_size()[0] - 1) + '\n'
    return commands


# УДАЛИТЬ: необходимо учиться читать и использовать чужой код (функция utils.header_text()) — всё своё с нуля никогда не напишете
def game_title() -> None:
    """Выводит заголовок игры"""
    width = get_terminal_size().columns -3
    title = f'\n#{"="*width}#\n#{" "*width}#\n#'
    title += f'{"Игра".center(width)}#\n#'  
    title += f'{"Крестики-Нолики".center(width)}' 
    title += f'#\n#{" "*width}#\n#{"="*width}#\n'    
    return print(title)

