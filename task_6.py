
a = abs(int(input("1-й день пробежки кол-во км")))
b = abs(int(input("результат")))
result_days = 1
result_km = a
while result_km < b:
    a = 1.1 * a
    result_days += 1
    result_km = result_km + a
print(f"day", result_days)
