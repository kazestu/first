
number = abs(int(input("right nuber")))
max = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    if number > 9:
        continue
    else:
        print("max nomber", max)
        break
