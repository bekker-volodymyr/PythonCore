print(range(10))
print(range(4, 12))
print(range(3, 9, 3))

print(type(range(10)))

var = 10
var2 = 'hello'

for i in range(5):
    print(i)

import random # імпорт всього модулю
from random import randint # імпорт конкретної складової модулю

random_number = random.randint(0, 10)
random_number = randint(0, 5)

random_even = random.randrange(0, 101, 2)
print(random_even)

for i in range(5):
    random_number = randint(0, 10)
    print(random_number)


counter = 0
while counter < 5:
    print(counter)
    counter_inner = 0
    while counter_inner < 3:
        print(f"\t{counter_inner}")
        counter_inner += 1
    counter += 1


for i in range(5):
    print(i)
    for j in range(3):
        print(f"\t{j}")