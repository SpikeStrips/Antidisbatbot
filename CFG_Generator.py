### ИМПОТРИРУЕМ
from random import randint
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

### ШАПКА (Текст в консоли)
time.sleep(1)
print(Fore.CYAN +'\n     CFG_Generator for Gmod v1.0 ')
print('       Author of work: SpikeStrips \n')
print(Style.RESET_ALL,end='')
time.sleep(1)
### ОСНОВНАЯ ИНФОРМАЦИЯ (Текст в консоли)
print(Fore.GREEN + 'Основная информация:'.upper())
print(Style.RESET_ALL,end='')
print('-------------------------------------------------------------------------------------------------------------')
print(Fore.RED + "Для генерации конфигурационного файла вам необходимо:")
print(Style.RESET_ALL,end='')
print("1.Указать полный путь к вашей папке с GMOD. Пример: 'D:\Steam\steamapps\common\GarrysMod'\n2.Ввести название (транслитом) для сгенерированного конфигурационного файла. Примеры: 'moetPol', 'Moet_steny' и т. д.\n3.Ввести нужное вам RP-действие(от 3 лица). Примеры: 'приседает'; 'моет пол'; 'протирает стену' и т. д.\n4.Указать кол-во совершаемых действий. Примеры: '200', '100', '1292' и т. д.")
print('-------------------------------------------------------------------------------------------------------------\n')
print(Fore.GREEN + 'ввод ваших данных:'.upper())
print(Style.RESET_ALL,end='')

### ЗАПРАШИВАЕМ ОТ ПОЛЬЗОВАТЕЛЯ ВХОДНЫЕ ДАННЫЕ (ПУТЬ)
Folder_path = input('Шаг #1 Укажите полный путь к своей папке с GMOD: '.upper())


### ПРОВЕРКА ПУТИ (folder_path)
 ## ЕСЛИ ПУТЬ ВЕРЕН
if 'steamapps\common\GarrysMod' in Folder_path:
    print('')
    print(Fore.GREEN +'Вы указали правильный путь!'.upper())
    print(Style.RESET_ALL)
    
 ## ЕСЛИ ПУТЬ НЕВЕРЕН  
else:
    while not('steamapps\common\GarrysMod' in Folder_path):
    
        # ОЧИЩАЕТ КОНСОЛЬ
        os.system('CLS')
        
        # ШАПКА (Текст в консоли)
        print(Fore.CYAN +'\n     CFG_Generator for Gmod v1.0 ')
        print('       Author of work: SpikeStrips \n')
        print(Style.RESET_ALL,end='')
        
        # ОСНОВНАЯ ИНФОРМАЦИЯ (Текст в консоли)
        print(Fore.GREEN + 'Основная информация:'.upper())
        print(Style.RESET_ALL,end='')
        print('-------------------------------------------------------------------------------------------------------------')
        print(Fore.RED + "Для генерации конфигурационного файла вам необходимо:")
        print(Style.RESET_ALL,end='')
        print("1.Указать полный путь к вашей папке с GMOD. Пример: 'D:\Steam\steamapps\common\GarrysMod'\n2.Ввести название (транслитом) для сгенерированного конфигурационного файла. Примеры: 'moetPol', 'Moet_steny' и т. д.\n3.Ввести нужное вам RP-действие(от 3 лица). Примеры: 'приседает'; 'моет пол'; 'протирает стену' и т. д.\n4.Указать кол-во совершаемых действий. Примеры: '200', '100', '1292' и т. д.")
        print('-------------------------------------------------------------------------------------------------------------\n')
        print(Fore.GREEN + 'ввод ваших данных:'.upper())
        print(Style.RESET_ALL,end='')
        print('')
        
        # СООБЩЕНИЕ ОБ ОШИБКЕ
        print(Fore.RED +'Вы где то допустили ошибку, попробуйте еще раз!'.upper())
        print(Style.RESET_ALL)
        Folder_path = input('Шаг #1 Укажите полный путь к своей папке с GMOD: '.upper())
    
    ## ЕСЛИ ПУТЬ НЕВЕРЕН
    print('')
    print(Fore.GREEN +'Вы указали правильный путь!'.upper())
    print(Style.RESET_ALL)

### ЗАПРАШИВАЕМ ОТ ПОЛЬЗОВАТЕЛЯ ВХОДНЫЕ ДАННЫЕ (НАЗВАНИЕ ФАЙЛА, НАЗВАНИЕ ДЕЙСТВИЯ, КОЛ-ВО ДЕЙСТВИЙ)
Config_name = input('Шаг #2 Введите название для вашего конфигурационного файла: ')
Roleplay_action = input('Шаг #3 Введите нужное РП-действие: ')
Number_of_actions = int(input('Шаг #4 Укажите цифрами точное кол-во этих действий: '))

### ПЕРЕХОДИМ В КОРНЕВУЮ ДИРЕКТОРИЮ С GMOD.
os.chdir(Folder_path)
os.chdir('garrysmod\cfg')

### СОЗДАЕМ В ЭТОЙ ДИРЕКТОРИИ ПУСТОЙ КФГ ФАЙЛ И ЗАДАЕМ ЕМУ КОДИРОВКУ.
Config_name_update = Config_name + '.cfg'
text_file = open(Config_name_update, "w",encoding="utf-8")

### ПРОПИСЫВАЕМ В НАШ КФГ ФАЙЛ ПЕРВЫЕ ДВЕ СТРОКИ
foundation = f'bind n {Config_name}\n'
text_file.write(foundation)
foundation_update = f'alias {Config_name} "say /me {Roleplay_action} 1; bind n {Config_name}1"\n'
text_file.write(foundation_update)

### ГЕНЕРИРУЕМ РАНДОМНЫЕ ЧИСЛА И ЗАПИСЫВАЕМ ИХ В ПЕРЕМЕННЫЕ (ДЛЯ ЦИКЛА)
random_number1 = randint(0, 60)
random_number2 = randint(61, 120)
random_number3 = randint(121, 180)
random_number4 = randint(181,240)
random_number5 = randint(241, 300)
random_number6 = randint(301, 360)
random_number7 = randint(361, 420)
random_number8 = randint(421, 480)
random_number9 = randint(481, 540)
random_number10 = randint(541, 600)
random_number11 = randint(601, 660)
random_number12 = randint(601, 660)
random_number13 = randint(661, 720)
random_number14 = randint(721, 780)
random_number15 = randint(781, 840)
random_number16 = randint(841, 900)
random_number17 = randint(901, 960)
random_number18 = randint(960, 1020)
random_number19 = randint(1021, 1080)
random_number20 = randint(1081, 1140)

### СОЗДАЕМ ПЕРЕМЕННЫЕ (ДЛЯ ЦИКЛА)
a = 0
number_left = 1
number_right = 2
number_center = 2

### ЦИКЛ (ПРОПИСЫВАЕМ В НАШ КФГ ФАЙЛ ОСТАЛЬНЫЕ СТРОКИ)
while a != Number_of_actions:
    foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center}; bind n {Config_name}{number_right}"\n'
    text_file.write(foundation_update)
    
    ### ДОБАВЛЯЕМ В КФГ НАМЕРЕННЫЕ ОШИБКИ
    if a == random_number1:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say \me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number2:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number3:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number4:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number5:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number6:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 3}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number7:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say \me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number8:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number9:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 4}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number10:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number11:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number12:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number13:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number14:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number15:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number16:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number17:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number18:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number19:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say /me {Roleplay_action} {number_center + 2}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)
    elif a == random_number20:
        number_left += 1
        number_right += 1
        foundation_update = f'alias {Config_name}{number_left} "say me {Roleplay_action} {number_center + 1}; bind n {Config_name}{number_right}"\n'
        text_file.write(foundation_update)

    number_left += 1
    number_right += 1
    number_center += 1
    a+=1

### ЗАВЕРШЕНИЕ ПРОГРАММЫ
time.sleep(4)
print(Back.RED + F"\n  Ваш конфигурационный файл под названием".upper(), "'"+Config_name_update+"'","был создан!!!".upper())
print(Style.RESET_ALL,end='\n')
time.sleep(3)
print('|=-->-->-->-->--> Программа автоматически закроется через: 5 сек')
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
time.sleep(3)
