date = int(input("Введите год рождения А.С. Пушкина: "))
print(date)

if date == 1799:
    print("Правильно")
    birthday = float(input("А Введите день рождения А.С. Пушкина: "))
    print(birthday)

    if birthday == 06.06:
        print("Верно")
    else:
        print("Неверный день рождения!")

else:
    print("Неверный год рождения!")


