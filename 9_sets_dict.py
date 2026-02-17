new_set = set() # функція-конструктор
my_set = set(['apple', 'banana', 'cherry'])

my_set = {'apple', 'banana', 'cherry', 'apple'}

print(', '.join(my_set))
print(type(my_set))

print(len(my_set)) # 3

new_set = {1, True, False, 0}
print(new_set) # False, 1

fruits_set = {'apple', 'banana', 'pineapple'}

for fruit in fruits_set:
    print(fruit)

print('apple' in fruits_set)
print('potato' not in fruits_set)

fruits_set.add('orange')
print(', '.join(fruits_set))
fruits_set.update(['mango', 'pamelo'])
print(', '.join(fruits_set))

fruits_set.remove('mango')
fruits_set.discard('orange')
fruits_set.pop()
print(', '.join(fruits_set))
fruits_set.clear()
print(fruits_set)

fruits = {'apple', 'banana', 'pineapple'}
vegies = {'tomato', 'potato'}

food = fruits.union(vegies)
food = fruits | vegies

print(', '.join(food))

fruits1 = {'apple', 'banana', 'pamelo'}
fruits2 = {'pamelo', 'orange', 'apple', 'kiwi'}

intersect = fruits1.intersection(fruits2)
intersect = fruits1 & fruits2
print(', '.join(intersect)) # pamelo, apple

diff = fruits1 - fruits2
print(', '.join(diff)) # banana
sym_diff = fruits1 ^ fruits2
print(', '.join(sym_diff)) # banana, orange, kiwi

frozen_fruits = frozenset({'apple', 'banana', 'kiwi'})
print(', '.join(frozen_fruits))
print(type(frozen_fruits))
# frozen_fruits.add('orange') # Помилка!

new_dictionary = dict() # функція-конструктор
new_dict = {
    'key': 'value',
    12: 12.4
}

contacts = {
    'Антон': '0505550960',
    'Настя': '0470995838'
}

contacts['Антон'] = '0670349548'
contacts['Сергій'] = '05505054039'

print(contacts['Антон'])
print(contacts['Сергій'])

for key in contacts: # перебір ключів
    print(f"{key}:{contacts[key]}")


for key in contacts.keys(): # перебір ключів
    print(key) 


for value in contacts.values(): # перебір значень
    print(value)


for pair in contacts.items(): # перебір пар ключ-значення
    print(pair)


contacts.pop('Антон')
contacts.popitem()
contacts.clear()

