date = ""
birthday = ""

while date != 1799:
    date = int(input("Введите год рождения А.С. Пушкина: "))

    if date < 1799:
        print("Попробуйте ещё раз")
    elif date > 1799:
        print("Попробуйте ещё раз")

print("Верно, идем дальше!")

while birthday != 06.06:
    birthday = float(input("А Введите день рождения А.С. Пушкина: "))

    if birthday > 06.06:
        print("Попробуйте ещё раз")
    elif birthday < 06.06:
        print("Попробуйте ещё раз")

print("Всё верно!")
