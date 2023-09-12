print("Добро пожаловать в Ксено-помощник v0.1 ! ")
input("Нажмите <ENTER> для продолжения")

#important values
total_nodes = 0
depth = 0
learned_nodes = 0
node_edges = 0
node_buffer = 0
node_status = "Н"
node_status_true = "Д"
node_status_false = "Н"
check_done = "Н"
check_depth = "Н"
status_true = "Д"
status_false = "Н"
#Node info

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

#Main cycle body

total_nodes = int(input("Сколько граней в узле ?: " ))
while learned_nodes != total_nodes:
    node_buffer += int(total_nodes)
    print("Текущая глубина узла: " + str(depth))
    node_status = input("Узел изучен? (Д/Н) ")
    if str.upper(node_status) == node_status_false : #Tier 0 Node
        print(steams_d0_showlist) 
        steams_type = input("Выберите тип стимуляции: ")
        if str.upper(steams_type) == str(steams_d0[0]):
            print(steams_d0_todo[0])
        elif str.upper(steams_type) == str(steams_d0[1]):
            print(steams_d0_todo[1])
        elif str.upper(steams_type) == str(steams_d0[2]):
            print(steams_d0_todo[2])
        check_done = input("Узел завершен? (Д/Н) ")
        if str.upper(check_done) == "Д":
            depth += 1
            learned_nodes += 1
    elif str.upper(node_status) == node_status_true :
        depth += 1

    print("Текущая глубина узла: " + str(depth))
    node_buffer = int(node_edges)
    node_edges = input("Введите кол-во граней нового узла: ")
    if node_buffer > 1 and int(node_edges) == 1:
        total_nodes -= 1
    if int(node_edges) != 1:
        total_nodes += int(node_edges)
    elif int(node_edges) == 1:
        total_nodes += 1
  
    node_status = input("Узел изучен? (Д/Н) ")
    if str.upper(node_status) == node_status_false : #Tier 1 Node
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
            
        check_done = input("Узел завершен? (Д/Н) ")
        if str.upper(check_done) == str.upper(status_true):
            depth += 1
            learned_nodes += 1
    elif str.upper(node_status) == node_status_true :
        depth += 1    

    print("Текущая глубина узла: " + str(depth))  
    node_buffer = int(node_edges)
    node_edges = input("Введите кол-во граней нового узла: ")
    if node_buffer > 1 and int(node_edges) == 1:
        total_nodes -= 1
    if int(node_edges) != 1:
        total_nodes += int(node_edges)
    elif int(node_edges) == 1:
        total_nodes += 1

    node_status = input("Узел изучен? (Д/Н) ")
    if str.upper(node_status) == node_status_false : #Tier 2 Node
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

        check_done = input("Узел завершен? (Д/Н) ")
        if str.upper(check_done) == str.upper(status_true):
            depth += 1
            learned_nodes += 1
    elif str.upper(node_status) == node_status_true :
        depth += 1

## Багуля в этом блоке. Если идет кол-во нод 1-2-1 (всего 3 ноды) - цикл не плюсует последнюю т.к. она считается на второй, но тут идет 1-2-2-1 и вот в 2-2-1 лишняя единица не вычитается, нужно что-то на подобии if node_buffer == node_eges > total_edges -= 1
    print("Текущая глубина узла: " + str(depth))  
    node_buffer = int(node_edges)
    node_edges = input("Введите кол-во граней нового узла: ")
    if node_buffer > 1 and int(node_edges) == 1:
        total_nodes -= 1
    if int(node_edges) != 1:
        total_nodes += int(node_edges)
    elif int(node_edges) == 1:
        total_nodes += 1

    node_status = input("Узел изучен? (Д/Н) ")
    if str.upper(node_status) == node_status_false : #Tier 3 Node
        print(steams_d3_showlist) 
        steams_type = input("Выберите тип стимуляции: ")
        if str.upper(steams_type) == str(steams_d3[0]):
            print(steams_d3_todo[0])
        elif str.upper(steams_type) == str(steams_d3[1]):
            print(steams_d3_todo[1])
        elif str.upper(steams_type) == str(steams_d3[2]):
            print(steams_d3_todo[2])
        elif str.upper(steams_type) == str(steams_d3[3]):
            print(steams_d3_todo[3])

        check_done = input("Узел завершен? (Д/Н) ")
        if str.upper(check_done) == str.upper(status_true):
            depth += 1
            learned_nodes += 1
    elif str.upper(node_status) == node_status_true :
        depth += 1

print("Total nodes: ", total_nodes) #DEBUG
print("Learned nodes:", learned_nodes ) #DEBUG
input("pause before end") #DEBUG
print("End of programm") #DEBUG