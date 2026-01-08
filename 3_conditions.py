# Умовні конструкції

# bool (boolean) - тип даних, що зберігає два значення - True або False
can_penguins_swim = True
can_penguins_fly = False

print(type(can_penguins_swim))
print(type(can_penguins_fly))
print("Чи може пінгвіни плавати:", can_penguins_swim)
print("Чи може пінгвіни літати:", can_penguins_fly)

# Оператори порівняння
number = int(input("Введіть ціле число: "))
print(f"{number} > 10? {number > 10}")
print(f"{number} < 10? {number < 10}")
print(f"{number} >= 10? {number >= 10}")
print(f"{number} <= 10? {number <= 10}")
print(f"{number} == 10? {number == 10}")
print(f"{number} != 10? {number != 10}")

'''

if <умова>:
    інструкція 1
    інструкція 2
    інструкція 3
    інструкція 4
    ...
else:
    інструкція 1
    інструкція 2
    ...

'''

weather = input("Введіть яка зараз погода: ")

if weather == "холодно":
    print("Вдягаю куртку")
    print("Вдягаю шапку")
else:
    print("Вдягаю футболку")
    print("Вдягаю кепку")

print("Виходжу на вулицю")

print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool("Hello, world"))
print(bool(123))
print(bool(-0.4))

print(f"{True}  and {True}   = {True and True}")
print(f"{True}  and {False}  = {True and False}")
print(f"{False} and {True}   = {False and True}")
print(f"{False} and {False}  = {False and False}")

print(f"{True}  or {True}   = {True or True}")
print(f"{True}  or {False}  = {True or False}")
print(f"{False} or {True}   = {False or True}")
print(f"{False} or {False}  = {False or False}")

number = int(input("Введіть ціле число: "))

if number >= 10 and number <= 20:
    print("Число в діапазоні від 10 до 20")
else:
    print("Число не потрапляє в діапазон від 10 до 20")

if number < 10 or number > 20:
    print("Число не в діапазоні від 10 до 20")
else:
    print("Число потрапляє в діапазон від 10 до 20")

print(f"{not True}")
print(f"{not False}")