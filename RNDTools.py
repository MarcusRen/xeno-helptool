from operator import truediv
from time import sleep

## TODO: разобраться заного с гранями и узлами и по итогу цикличностью каждого узла, при этом желательно разобраться еще и с делеями сообщений
## DID: Отказался от создания массивов данных вначале и вызова их в циклах на первое время, так проще ориентироваться в блоках цикла, возможно в будующем переедут отдельно от циклов


print("Добро пожаловать в Ксено-помощник v0.1 ! ")
edge_values = int(input("Сколько граней в узле ?: " ))
depth = 0
learned_edges = 0
check_done = "Н"
while edge_values != int(learned_edges):
    while check_done == "Н" and depth == 0: ## Модуль глубины == 0
        steams_d0_showlist = ["(Ф)изические повреждения", "(И)спользование инструментов", "(Э)лектричество"]
        steams_d0 = ["Ф", "И", "Э"]
        steams_d0_todo = ["Артефакт активируется от любого физического взаимодействия", "Закрепите артефакт гаечным ключом", "Используйте на артефакте мультитул, подключите его к проводам или ударьте включённой электродубинкой"]
        print(steams_d0_showlist)
        steams_type = input("Выберите тип стимуляции: ")
        if str.upper(steams_type) == str(steams_d0[0]):
            print(steams_d0_todo[0])
        elif str.upper(steams_type) == str(steams_d0[1]):
            print(steams_d0_todo[1])
        elif str.upper(steams_type) == str(steams_d0[2]):
            print(steams_d0_todo[2])
        print("Текущая глубина узла: " + str(depth))
        check_done = input("Узел завершен ? (Д): ")
        if str.upper(check_done) == "Д":
            depth += 1
            learned_edges += 1
            sleep (1)
            print("Переходим к следующему узлу")
            sleep(1)
    check_done = "Н"
    while check_done == "Н" and depth == 1: ## Модуль глубины == 1
        steams_d1_showlist = ["(З)вуковые вибрации", "(Ф)изические повреждения", "(А)ктивное замедление", "высокая (Т)емпература", "(В)одочувствительность"]
        steams_d1 = ["З", "Ф", "А", "Т", "В"]
        steams_d1_todo = ["Откройте UI музыкального инструмента, находясь недалеко от артефакта", "Нанесите 50 brute (механического) урона артефакту", "Бросьте артефакт, чтобы узел активировался от приземления", "Нагрейте воздух вокруг артефакта, либо кликните включённым сварочным аппаратом по нему.", "Опрысните артефакт водой"]
        print(steams_d1_showlist)
        steams_type = input("Выберите тип стимуляции: ")
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
        print("Текущая глубина узла: " + str(depth))
        check_done = input("Узел завершен ? (Д): ")
        if str.upper(check_done) == "Д":
            learned_edges += 1
        skip = False
        if int(learned_edges) == edge_values:
            skip = True
        elif skip == False:
            check_depth = input("Ушли вглубь ? (Д): ")
            if str.upper(check_depth) == "Д":
                depth += 1
                sleep(1)
                print("Переходим к следующему узлу")
                sleep(1)
            else:
                depth -= 1
                sleep(1)
                print("Переходим к предыдущему узлу")
                sleep(1)
    check_new_edges = input("Кол-во граней в узле: ")
    if int(check_new_edges) == 1:
        print("2 узла - пиздец не повезло")
    else: 
        edge_values += (int(check_new_edges) - 1)
    check_done = "Н"
    while check_done == "Н" and depth == 2:  ## Модуль глубины == 2
        steams_d2_showlist = ["эссенция (Ж)изни", "(М)агнитное поле", "экстремальное (Д)авление", "(С)тандартные атмосферные газы"]
        steams_d2 = ["Ж", "М", "Д", "С"]
        steams_d2_todo = ["Артефакт отреагирует на смерть любого живого существа поблизости", "Активируйте магнитные ботинки или магнит утилизации поблизости.", "Артефакт отреагирует, если находится в среде с давлением ниже 50 кПа.", "Артефакт отреагирует при попадании в среду с кислородом, азотом или углекислым газом (диоксидом углерода)."]
        print(steams_d2_showlist)
        steams_type = input("Выберите тип стимуляции: ")
        if str.upper(steams_type) == str(steams_d2[0]):
            print(steams_d2_todo[0])
        elif str.upper(steams_type) == str(steams_d2[1]):
            print(steams_d2_todo[1])
        elif str.upper(steams_type) == str(steams_d2[2]):
            print(steams_d2_todo[2])
        elif str.upper(steams_type) == str(steams_d2[3]):
            print(steams_d2_todo[3])
        print("Текущая глубина узла: " + str(depth))
        check_done = input("Узел завершен ? (Д): ")
        if str.upper(check_done) == "Д":
            learned_edges += 1
        skip = False
        if int(learned_edges) == edge_values:
            skip = True
        elif skip == False:
            check_depth = input("Ушли вглубь ? (Д): ")
            if str.upper(check_depth) == "Д":
                depth += 1
                sleep(1)
                print("Переходим к следующему узлу")
                sleep(1)                
            else:
                depth -= 1
                sleep(1)
                print("Переходим к предыдущему узлу")
                sleep(1)                
    check_new_edges = input("Кол-во граней в узле: ")
    edge_values += (int(check_new_edges) - 1)
    check_done = "Н"
else:
    print("Артефакт изучен")
    sleep (10)
    