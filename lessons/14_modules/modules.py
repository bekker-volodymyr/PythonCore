import math
import random

r = random.randint(10, 15)
f = math.factorial(20)

# from math import factorial
# from random import randint

# r = randint(10, 15)
# f = factorial(20)

# print(f"Random number: {r}\nFactorial of 20: {f}")

print(random.randint(1, 10))
print(random.randrange(0, 101, 10))
print(random.random())
print(random.uniform(1.5, 5.5))

colors = ['червоний', 'зелений', 'синій']
print(random.choice(colors))

print(random.choices(['яблуко', 'банан'], weights=[10, 1], k=3))

numbers = [1, 2, 3, 4, 5]
print(random.sample(numbers, 3))

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)

print(math.ceil(4.2))
print(math.floor(4.8))
print(math.trunc(-4.8))
print(math.fabs(-5))

print(math.sqrt(16))
print(math.pow(2, 3))

# Знаходимо синус кута 90 градусів
rad = math.radians(90)
print(math.sin(rad))    # Результат: 1.0

print(math.factorial(5)) # Результат: 120 (1*2*3*4*5)
print(math.gcd(36, 24))  # Результат: 12
print(math.isclose(0.1 + 0.2, 0.3)) # Результат: True

import my_module as my

my.greeting()
print(my.MODULE_CONST_INT)
print(my.MODULE_CONST_STR)
print(my.module_dict["key1"])