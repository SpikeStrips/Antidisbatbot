# Импорт зависимостей
import pyautogui
import pydirectinput
from random import randint
import time
import keyboard
import sys
import colorama
from playsound import playsound
from colorama import Fore, Back, Style
colorama.init()
import os

# Шапка (Текст в консоли)
print(Fore.CYAN +'\n     Antidisbat Bot v1.0 ')
print('       Author of work: SpikeStrips')
print(Style.RESET_ALL,end='\n')
print('-------------------------------------------------------------------------------------------------------------')

# Основная информация (Текст в консоли)
print(Fore.GREEN + '  Основные комбинации клавиш:'.upper())
print(Style.RESET_ALL,end='')
print('    1. Ctrl + 1 - Запустить бота!' )
print('    2. Ctrl + 2 - Остановить бота!' )
print('    3. Ctrl + 3 - Закрыть программу!' )
print('-------------------------------------------------------------------------------------------------------------\n')

# Стату бота (Текст в консоли)
list = {'on':' бот запущен!','off':'бот приостановлен!'}
print('  статус бота: '.upper(),end='')
print(Fore.YELLOW +'готов к работе!'.upper())
print(Style.RESET_ALL,end='')


def start():
    # Очищает консоль
    os.system('CLS')
    # Шапка (Текст в консоли)
    print(Fore.CYAN +'\n     Antidisbat Bot v1.0 ')
    print('       Author of work: SpikeStrips')
    print(Style.RESET_ALL,end='\n')
    print('-------------------------------------------------------------------------------------------------------------')
    # Основная информация (Текст в консоли)
    print(Fore.GREEN + '  Основные комбинации клавиш:'.upper())
    print(Style.RESET_ALL,end='')
    print('    1. Ctrl + 1 - Запустить бота!' )
    print('    2. Ctrl + 2 - Остановить бота!' )
    print('    3. Ctrl + 3 - Закрыть программу!' )
    print('-------------------------------------------------------------------------------------------------------------\n')
    # Стату бота (Текст в консоли)
    print('  статус бота:'.upper(),end='')
    print(Fore.GREEN + list['on'].upper())
    print(Style.RESET_ALL,end='')
    playsound('sounds\Sound_08537.mp3')
    
    # Запуск бота
    while keyboard.is_pressed('Ctrl + 2') == False:
        # Генерирует случайное время для каждого рп действие (время выбирается в диопазоне от 1 до 3 секунд)
        random_number = randint(1, 3)
        
        # Эмулирает нажатие клавиши Y (тем самым создает анимацию в игре)
        pydirectinput.keyDown('y')
        time.sleep(random_number)
        pydirectinput.keyUp('y')
        
        # Эмулирает нажатие клавиши ENTER (тем самым заканчивает анимацию в игре)
        pyautogui.press('enter')
        pydirectinput.keyDown('n')
        time.sleep(1)
        
        # Эмулирает нажатие клавиши N (тем самым выполняет одно рп действие)
        pydirectinput.keyUp('n')


def stop():
    # Очищает консоль
    os.system('CLS')
    # Шапка (Текст в консоли)
    print(Fore.CYAN +'\n     Antidisbat Bot v1.0 ')
    print('       Author of work: SpikeStrips')
    print(Style.RESET_ALL,end='\n')
    print('-------------------------------------------------------------------------------------------------------------')
    # Основная информация (Текст в консоли)
    print(Fore.GREEN + '  Основные комбинации клавиш:'.upper())
    print(Style.RESET_ALL,end='')
    print('    1. Ctrl + 1 - Запустить бота!' )
    print('    2. Ctrl + 2 - Остановить бота!' )
    print('    3. Ctrl + 3 - Закрыть программу!' )
    print('-------------------------------------------------------------------------------------------------------------\n')
    # Стату бота (Текст в консоли)
    print('  статус бота:'.upper(), Fore.RED + list['off'].upper())
    playsound('sounds\Sound_22471.mp3')
    time.sleep(1)
    print(Style.RESET_ALL,end='')
    
# Клавиши для взаимодействие с ботом
keyboard.add_hotkey('Ctrl + 1', start)
keyboard.add_hotkey('Ctrl + 2', stop)
keyboard.wait('Ctrl + 3')

# Завершение программы (Текст в консоли)
print('\033[31m' + '\n   завершение работы!!!'.upper())
playsound('sounds\Sound_04573.mp3')
print(Style.RESET_ALL,end='')
print('\n|=-->-->-->-->--> Программа автоматически закроется через: 5 сек')
time.sleep(1)
print('|=-->-->-->--> Программа автоматически закроется через: 4 сек')
time.sleep(1)
print('|=-->-->--> Программа автоматически закроется через: 3 сек')
time.sleep(1)
print('|=-->--> Программа автоматически закроется через: 2 сек')
time.sleep(1)
print('|=--> Программа автоматически закроется через: 1 сек')
time.sleep(1)
print('\n        Спасибо за использование нашей программы!\n'.upper())
time.sleep(1)
print('    c=3, c=3, c=3, c=3, c=3, c=3, c=3, c=3, c=3, c=3, c=3, c=3 ')
time.sleep(2)



