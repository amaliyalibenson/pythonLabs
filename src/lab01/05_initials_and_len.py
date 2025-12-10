s = str(input("ФИО: "))
otvet = ""
otvet2 = 0
for i in s:
    # прохожусь по строке
    if i.isupper():
        otvet += i
        # если попался верхний регистр, то его записываю в ответ
    if i != " ":
        otvet2 += 1
        # считаю символы без лишних пробелов

print(otvet2 + 2, otvet + ".")
