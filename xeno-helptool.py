import time
import os

programm_end = 0
needed_depth = 0
cycle_status =  "Д"
check_positive = "Д"
check_negative = "Н" 


#LVL 0 Node
steams_d0_showlist = ["(Ф)изические повреждения", "(И)спользование инструментов", "(Э)лектричество"]
steams_d0 = ["Ф", "И", "Э"]
steams_d0_todo = ["Артефакт активируется от любого физического взаимодействия", "Закрепите артефакт гаечным ключом", "Используйте на артефакте мультитул, подключите его к проводам или ударьте включённой электродубинкой"]

#LVL 1 Node
steams_d1_showlist = ["(З)вуковые вибрации", "(Ф)изические повреждения", "(А)ктивное замедление", "высокая (Т)емпература", "(В)одочувствительность"]
steams_d1 = ["З", "Ф", "А", "Т", "В"]
steams_d1_todo = ["Откройте UI музыкального инструмента, находясь недалеко от артефакта", "Нанесите 50 brute (механического) урона артефакту", "Бросьте артефакт, чтобы узел активировался от приземления", "Нагрейте воздух вокруг артефакта, либо кликните включённым сварочным аппаратом по нему.", "Опрысните артефакт водой"]

#LVL 2 Node
steams_d2_showlist = ["эссенция (Ж)изни", "(М)агнитное поле", "экстремальное (Д)авление", "(С)тандартные атмосферные газы"]
steams_d2 = ["Ж", "М", "Д", "С"]
steams_d2_todo = ["Артефакт отреагирует на смерть любого живого существа поблизости", "Активируйте магнитные ботинки или магнит утилизации поблизости.", "Артефакт отреагирует, если находится в среде с давлением ниже 50 кПа.", "Артефакт отреагирует при попадании в среду с кислородом, азотом или углекислым газом (диоксидом углерода)."]

#LVL 3 Node
steams_d3_showlist = ["(Ф)изические повреждения", "(Р)адиация", "(Э)кстремальное давление", "(Г)азообразная плазма"]
steams_d3 = ["Ф", "Р", "Э", "Г"]
steams_d3_todo = ["Нанесите артефакту 500 brute (механического) урона.", "Артефакт отреагирует при получении 50 урона от радиации.", "Артефакт должен находиться в среде с давлением выше 385 кПа", "Артефакт отреагирует при попаданию в среду с газообразной плазмой."]

os.system("mode con cols=130 lines=3")

os.system('cls')
print("o/")
print("Добро пожаловать в Ксено-помощник v0.3 ! ")
input("Нажмите <ENTER> для продолжения")
os.system('cls')

while programm_end == 0:
    print(" ")
    needed_depth = input("Введите требуемую глубину узла: ")
    print(" ")
    os.system('cls')

    if int(needed_depth) == 0 : #Tier 0 Node
        print("Типы стимуляции артефакта:")
        print(steams_d0_showlist) 
        steams_type = input("Выберите необходимый тип: ")
        os.system('cls')
        print("Решение найдено:")
        if str.upper(steams_type) == str(steams_d0[0]):
            print(steams_d0_todo[0])
        elif str.upper(steams_type) == str(steams_d0[1]):
            print(steams_d0_todo[1])
        elif str.upper(steams_type) == str(steams_d0[2]):
            print(steams_d0_todo[2])
        input("Для продолжения нажмите <ENTER>")
        os.system('cls')


    if int(needed_depth) == 1 : #Tier 1 Node
        print("Типы стимуляции артефакта:")
        print(steams_d1_showlist) 
        steams_type = input("Выберите необходимый тип: ")
        os.system('cls')
        print("Решение найдено:")
        if str.upper(steams_type) == str(steams_d1[0]):
            print(steams_d1_todo[0])
        elif str.upper(steams_type) == str(steams_d1[1]):
            print(steams_d1_todo[1])
        elif str.upper(steams_type) == str(steams_d1[2]):
            print(steams_d1_todo[2])
        elif str.upper(steams_type) == str(steams_d1[3]):
            print(steams_d1_todo[3])
        elif str.upper(steams_type) == str(steams_d1[4]):
            print(steams_d1_todo[4])
        input("Для продолжения нажмите <ENTER>")
        os.system('cls')

        
    if int(needed_depth) == 2 : #Tier 2 Node
        print("Типы стимуляции артефакта:")
        print(steams_d2_showlist) 
        steams_type = input("Выберите необходимый тип: ")
        os.system('cls')
        print("Решение найдено:")
        if str.upper(steams_type) == str(steams_d2[0]):
            print(steams_d2_todo[0])
        elif str.upper(steams_type) == str(steams_d2[1]):
            print(steams_d2_todo[1])
        elif str.upper(steams_type) == str(steams_d2[2]):
            print(steams_d2_todo[2])
        elif str.upper(steams_type) == str(steams_d2[3]):
            print(steams_d2_todo[3])
        input("Для продолжения нажмите <ENTER>")
        os.system('cls')


    if int(needed_depth) == 3 : #Tier 3 Node
        print("Типы стимуляции артефакта:")
        print(steams_d3_showlist) 
        steams_type = input("Выберите необходимый тип: ")
        os.system('cls')
        print("Решение найдено:")
        if str.upper(steams_type) == str(steams_d3[0]):
            print(steams_d3_todo[0])
        elif str.upper(steams_type) == str(steams_d3[1]):
            print(steams_d3_todo[1])
        elif str.upper(steams_type) == str(steams_d3[2]):
            print(steams_d3_todo[2])
        elif str.upper(steams_type) == str(steams_d3[3]):
            print(steams_d3_todo[3])
        input("Для продолжения нажмите <ENTER>")
        os.system('cls')

    print(" ")
    cycle_status = input("Дальнейшие изучение требуется ? Д/Н: ")
    print(" ")
    if str.upper(cycle_status) == check_positive:
        os.system('cls')
        print(" ")
        print("Переходим к новому узлу, нажмите <ENTER>")
        input()
        os.system('cls')

        programm_end = 0
    else:
        os.system('cls')
        programm_end = 1

print(" ")
print("Поздравляем с завершением изучения артефакта!")
time.sleep(1)
os.system('cls')