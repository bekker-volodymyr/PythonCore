# Типи даних
print(type(10))     # int
print(type(4.6))    # float
print(type(10 / 4)) # float - результат виразу має тип даних float
print(type("text")) # str

# Змінні
numbers_sum = 10 + 12
print(numbers_sum)

numbers_sum = 5 + 1 # старе значеня видаляється та записується нове
print(numbers_sum)

number = 10
print(number)
# збільшуємо значення на 5
number += 5 # number = number + 5
print(number)

# скорочені оператори присвоєння
number += 5
number -= 5
number *= 5
number /= 5
number %= 5
number //= 5
number **= 5

# Форматований вивід даних
print(f"5 + 5 = {5 + 5}")
num = 10 + 2
print(f"Значення змінної num дорівнює {num}")

# Введення даних
user_name = input("Введіть своє ім'я: ")
print("Привіт, ", user_name)

user_age = input("Введіть ваш вік: ")
print("Вам", user_age, "років")

# Функції-конструктори
variable_int = int()
variable_float = float()
variable_str = str()

var_int = int('10')
var_float = float('8.9')
var_str = str(10)

print(f"{var_int} {type(var_int)}")
print(f"{var_float} {type(var_float)}")
print(f"{var_str} {type(var_str)}")

# Перетворення типів
num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

print(type(num1))
print(type(num2))

num1 = int(num1)   # перетворення в int
num2 = float(num2) # перетворення в float
print(type(num1))
print(type(num2))

print(f"{num1} * {num2} = {num1 * num2}")



