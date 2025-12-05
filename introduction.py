
print("Hello, World!")
print("Hello,", "Vova!")

print(1, 2, 3, 4, 5, 6, 7)
print(1, 3, 4, 5, 6, sep="; ")
print("Багато", "різних", "значень", 999, 134)

print("Цей print на одному рядку з наступним.", end=" ")
print("Наступний print")

print("Кафе \"Птах\".")
print('\'Текст в одиночних лапках\'.')
print("\tТекст з відступом.")
print("Текст, що розбитий\nна два рядки.")
print("\\ - симовл з якого починаються escape-послідовності.")

print(r"C:\Users\ITStep\PythonCore") # raw-рядок


# однорядковий коментар

'''
Багаторядковий 
коментар
'''

'''
print(10 + 43)
print(15 * 2 + 5)
print(10 / 13 + (12 + 4) / 5)

print("10 + 10 =", 10 + 10)
print("10 - 5 =", 10 - 5)
print("10 * 3 =", 10 * 3)
print("10 / 3 =", 10 / 3)
print("10 % 3 =", 10 % 3)
print("10 // 3 =", 10 // 3)
print("3 ** 2 =", 3 ** 2)
'''

'''
print(type(10))     # int
print(type(4.6))    # float
print(type(10 / 4)) # float
print(type("text")) # str
'''

'''
numbers_sum = 10 + 12
print(numbers_sum)

numbers_sum = 5 + 1
print(numbers_sum)
'''

user_name = input("Введіть своє ім'я: ")
print("Привіт, ", user_name)

user_age = input("Введіть ваш вік: ")
print("Вам", user_age, "років")