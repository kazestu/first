
a = abs(int(input("Выручка")))
b = abs(int(input("Издежки")))
if a > b:
    print("Прибыль состовляет", a / (a-b))
    c = abs(int(input("Количество сотрудников")))
    print("Прибыль на каждого сотрудника", (a / (a-b)) / c)
else:
    a < b
    print("Убытки")
