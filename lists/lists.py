# lists | списки

# if-elif-else
# умовні оператори які дозволяють виконувати різні алгоритми дій 
# в залежності від умови

# match-case
# перевіряє значення змінної

# number = int(input("Enter number: "))

# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print("Number is negative")

# match number:
#     case 0: print("Number is null")
#     case 1: print("Number is one")
#     case _: print("Number is not null and not one")

# counter = 0
# while counter < 20:
#     print(counter)
#     counter += 1
# else:
#     print("Цикл завершився природним чином.")

# sum = 0
# while True:
#     number = int(input("Enter new number: "))
#     sum += number
#     quit = input("Enter q to quit: ")
#     if quit == 'q':
#         break

# print(sum)

# min = -21
# max = 19
# counter = min
# while counter <= max:
#     counter += 1
#     if counter % 4 == 0: # пропускаємо кратні 4
#         continue
#     print(counter)

# number = 10
# numbers = [10, 45, 54, 32]
# print(len(numbers)) # 4 елементи
# # додати значення змінної number до списку numbers
# numbers.insert(2, number)
# numbers.append(23)
# print(len(numbers)) # 6 елементів
# print(numbers)
# print(numbers[3])
# numbers.pop(4) # видалити по індексу
# print(len(numbers)) # 5 елементів
# numbers.remove(23) # видалити за значенням
# print(numbers)
# numbers.clear()
# print(numbers)
# print(len(numbers)) # 0 елементів

# Запитати у користувача 5 чисел
# Підрахувати кількість чисел кратних 4, 5 та кількість від'ємних чисел
# Вивести на екран числа у відповідній категорії 
# (тобто окремо вивести всі числа кратні 4, окремо кратні 5 та окремо від'ємні)
# Приклад:
# Користувач вводить: 10 -4 65 20 41
# Кратні 4: [-4, 20], Кількість: 2
# Кратні 5: [10, 65, 20], Кількість: 3
# Від'ємні: [-4], Кількість: 1

# numbers = list()
# mult4 = list()
# mult5 = list()
# negative_nums = list()
# # count4 = 0
# # count5 = 0
# # count_negative = 0
# counter = 0

# while counter < 5:
#     # next_number = int(input("Enter number: "))
#     numbers.append(int(input("Enter number: ")))
#     counter += 1

# counter = 0

# while counter < len(numbers):
#     if numbers[counter] % 4 == 0:
#         # count4 += 1
#         mult4.append(numbers[counter])
#     if numbers[counter] % 5 == 0:
#         #count5 += 1
#         mult5.append(numbers[counter])
#     if numbers[counter] < 0:
#         #count_negative += 1
#         negative_nums.append(numbers[counter])
#     counter += 1

# print(f"Кратні 4: {mult4}, Кількість: {len(mult4)}")
# print(f"Кратні 5: {mult5}, Кількість: {len(mult5)}")
# print(f"Від'ємні: {negative_nums}, Кількість: {len(negative_nums)}")

# import random

# rand_num = random.random() # випадкове число від 0 до 1
# print(rand_num)

# print(random.randint(1, 10)) # випдакове ціле число (включно)

# fruits = ['яблуко', 'банан', 'груша', 'полуниця', 'виноград', 'гранат']
# print(random.choice(fruits))

# # random.shuffle(fruits)
# print(fruits)

# # slicing
# print(fruits[0:3]) # отримати елементи від 0(включно) індекса до 3 (не включно)
# print(fruits[3:5]) # отримати елементи від 3 до 5 (не включно з 5)
# print(fruits[:4]) # від 0 до 4
# print(fruits[3:]) # від 3 до кінця
# print(fruits[1:3]) # від 1 до 3 
# print(fruits[0::2]) # від початку (0 елемента) до кінця кожен другий
# print(fruits[1::2]) # від 1 до кінця кожен другий
# print(fruits[0:5:3]) # від початку, до 5 елемента, кожен третій
# print(fruits[1:5:2]) # від 1 елемента, до 5 елемента, кожен другий
# print(fruits[::-1]) # всі елементи від кінця до початку (зворотній порядок)

fruits = ['яблуко', 'банан', 'груша', 'полуниця', 'виноград', 'гранат']

# and or not
# not
# True -> False
# False -> True

print('гранат' not in fruits)
print('абрикос' in fruits)

vegies = ['помідор', 'цибуля', 'огірок',  'болгарський перець']

food = fruits + vegies
print(food)

# Типи даних - характеристика даних, яка визначає 
# 1) які значення ми можемо зберігати
# 2) які операції можемо виконувати

# int - цілі числа (+ - / * // % ** < > <= >= == !=)
# float - дробові числа (+ - / * // % ** < > <= >= == !=)
# str - текст, послідовність символів (+ *(на ціле число))
# bool - True або False (and or not)
# list - можемо зберігати набір значень різного типу (+ *(на ціле число))

# nums = [12, 4, 5, 6]
# print(nums * 4)

# # вкладені списки
# table = [
#     [12, 3, 6, 7],      # 0
#     [11, 10, 8, 12],    # 1
#     [10, 9, 10, 1],     # 2
#     [12, 4, 5, 2]       # 3
# ]

# print(table[2])
# table[2][3] = 10
# print(table[2])

# list3d = [
#     [ # 0
#         [10, 23, 45, 1], # 0
#         [43, 56, 67, 1] # 1
#     ],
#     [ # 1
#         [54, 65, 1] # 0
#     ],
#     [ # 2
#         [54, 65, 65] # 0
#     ]
# ]

# print(list3d[0][1][2])
# print(list3d[0][1])
# print(list3d[1][0])
# print(list3d[0], list3d[2])

# my_list = []

# user_list = [10, 23, 34]
# user_list2 = [43, 54, 0]
# my_list.append(user_list)
# my_list.append(user_list2)

# print(my_list)

'''
Завдання 1
Користувач вводить імена студентів, які додаються в список.
Далі користувач вводить ім'я студента, присутність якого треба перевірити.
Програма виводить "Студент {ім'я} присутній" якщо студент є у списку. 
Якщо студента нема в списку програма виводить "Студент {ім'я} відсутній"
'''

'''
Завдання 2. Гра "Вгадай число"
Програма загадує випадкове число в діапазоні від 0 до 500.
Далі програма запитує у користувача спробу вгадати число.
Якщо загадане число менше за вказане користувачем програма дає відповідну підказку (загадане число менше)
І навпаки.
Програма зберігає всі числа які користувач вводив і рахує кількість спроб вгадати число.
Коли користувач вгадав число програма виводить на екран всі його спроби та кількість цих спроб.
Наприклад:
Загадане число: 43
1 спроба: 23
Відповідь програми: загадане число більше
2 спроба: 45
Відповідь програми: загадане число менше
3 спроба: 43
Відповідь програми: Ви вгадали! Спроби: [23, 45, 43], кількість: 3
'''