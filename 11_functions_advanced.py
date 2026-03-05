def get_discounted_prices(prices):
    discounted_prices = []  # Створюємо локальний стан
    
    for price in prices:
        if price > 100:
            new_price = price * 0.8
            discounted_prices.append(new_price) # Мутуємо стан крок за кроком
            
    return discounted_prices

# Викликаємо нашу процедуру
original_prices = [50, 120, 80, 200, 300]
result = get_discounted_prices(original_prices)

# прямий виклик
def recursion(): 
    print('recursion')
    recursion()

# recursion()

# опосередкований виклик
def func_a():
    print('a calls b')
    func_b()

def func_b():
    print('b calls a')
    func_a()

# func_a()

def factorial_rec(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)
    

# print(factorial_rec(5))


def factorial_loop(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# print(factorial_loop(5))

def callback():
    print('Hello')


func_var = callback
print(type(func_var))
func_var()


def some_function(callback):
    print('Some function that calls another function')
    callback()


some_function(callback)


sum = lambda a, b: a + b

sum(10, 12)

operations = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b
}

num1 = float(input('Введіть перше число: '))
num2 = float(input('Введіть перше число: '))

action = input('Оберіть дію (+, -, *): ')

if action in operations:
    print(operations[action](num1, num2))


tax_rate = 0.2  # Глобальна змінна

def calculate_tax_impure(amount):
    # Функція залежить від зовнішнього стану. Якщо хтось змінить tax_rate, 
    # результат функції зміниться, хоча аргумент amount залишиться тим самим.
    return amount * tax_rate


def calculate_tax_pure(amount, tax_rate):
    # Усе, що потрібно для обчислення, передається всередину.
    # Жодних сюрпризів.
    return amount * tax_rate


def add_product_impure(cart, product):
    # Функція бере існуючий список і змінює його (мутує).
    # Це побічний ефект, бо оригінальний масив за межами функції назавжди змінився.
    cart.append(product) 
    return cart

my_cart = ["apple", "banana"]
add_product_impure(my_cart, "orange")


def add_product_pure(cart, product):
    # Функція створює НОВУ копію списку, залишаючи оригінал недоторканим.
    new_cart = cart.copy() 
    new_cart.append(product)
    return new_cart

my_cart = ["apple", "banana"]
new_cart = add_product_pure(my_cart, "orange")
# Оригінальний my_cart залишився ["apple", "banana"]
# Ми отримали новий список new_cart із доданим апельсином

def create_multiplier(factor):
    # Створюємо внутрішню функцію, яка "запам'ятовує" переданий factor
    def multiplier(number):
        return number * factor
    
    # Повертаємо саму ФУНКЦІЮ, а не результат її виконання (без дужок)
    return multiplier

# Створюємо дві НОВІ функції за допомогою нашої функції вищого порядку
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Виведе 10
print(triple(5))  # Виведе 15


numbers = [15, 8, 42, 4, 16, 23]

filtered_iterator = filter(lambda a: a % 2 == 0, numbers)

even_numbers = list(filtered_iterator)

print("Оригінал:", numbers)
print("Результат:", even_numbers) # Виведе: [8, 42, 4, 16]


# Наші початкові дані (оригінальний стан)
prices = [50, 120, 80, 200]

# 1. Описуємо чисту функцію перетворення
def apply_discount(price):
    return price * 0.8  # Застосовуємо знижку 20%

# 2. Використовуємо map (передаємо функцію як аргумент)
# Ми кажемо ЩО зробити з кожним елементом, а не ЯК йти по списку
mapped_iterator = map(apply_discount, prices)

# Перетворюємо ітератор у звичайний список
discounted_prices = list(mapped_iterator)

print("Оригінальні ціни:", prices)
print("Ціни зі знижкою:", discounted_prices) # Виведе: [40.0, 96.0, 64.0, 160.0]


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())