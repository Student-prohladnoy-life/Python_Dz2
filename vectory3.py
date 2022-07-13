kol = 0
vsego = 5

print(F'{"<" * 9} Добро пожаловать на викторину {">" * 9}')

while True:
    print(F'{"<" * 20} НАЧНЁМ! {">" * 20}')

    vpr = input("День рождения А.С Пушкина?"'\n')  # 1799
    if vpr == "1799":
        print("Верно")
        kol = kol + 1
    else:
        print("Не верно")

    vpr = input("День рождения А.А. Блока?"'\n')  # 1880
    if vpr == "1880":
        print("Верно")
        kol = kol + 1
    else:
        print("Не верно")

    vpr = input("День рождения А.П. Чехова?"'\n')  # 1860
    if vpr == "1860":
        print("Верно")
        kol = kol + 1
    else:
        print("Не верно")

    vpr = input("День рождения С.А. Есенина?"'\n')  # 1895
    if vpr == "1895":
        print("Верно")
        kol = kol + 1
    else:
        print("Не верно")

    vpr = input("День рождения В.В. Маяковского?'\n")  # 1893
    if vpr != "1893":
        print(" Не верно")
        pass
    else:
        print("Верно")
        kol = kol + 1

    result = kol * 100 / 5
    result2 = 100 - result
    print(kol, "Верных ответов")
    print(5 - kol, " Не верных ответов")
    print("Верных ответов:", result, "%")
    print("Не верных ответов:", result2, "%")
    print("Ответы приняты!")

    answer = input("Повторим? (да / нет):"'\n').lower()
    if answer == "нет":
        break

print("До свидания!")
