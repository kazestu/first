
seconds = int(input("введите секунды"))
hoers_for_clock = (seconds//3600)
minutes = (seconds%3600)
minutes_for_clock = (minutes//60)
seconds_for_clock = (minutes_for_clock%60)
str_second = f"{hoers_for_clock:02}:{minutes_for_clock:02}:{seconds_for_clock:02}"
print(str_second)
