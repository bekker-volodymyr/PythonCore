# Пусті списки
collection = list()
collection = []

print(type(collection))

# Список з елементами
items = [10, 12.5, 'text', True]
fruits = ['apple', 'kiwi', 'mango', 'banana', 'avocado']

print(fruits)

print(items[0]) # 10
print(items[2]) # 'text'
# print(items[15]) # Помилка

print(fruits[:4])
print(fruits[1:3])
print(fruits[3:])
print(fruits[2:4:2])
print(fruits[::3])

print(fruits[-1])
print(fruits[-3])

print(fruits[-1:-4:-1])
print(fruits[:-2:-1])
print(fruits[::-1])

fruits[2] = 'pamelo' # mango -> pamelo

print(fruits[2]) # pamelo

print(len(items)) # 4
print(len(fruits)) # 5

counter = 0
while counter < len(fruits):
    print(fruits[counter], ' ')
    counter += 1

print()

for fruit in fruits:
    print(fruit, end=' ')

print()

# Вивід: apple, kiwi, pamelo, banana, avocado
print(', '.join(fruits))

fruits.append('orange')
print(', '.join(fruits))
fruits.extend(['mandarin', 'pear'])
print(', '.join(fruits))
fruits.insert(2, 'lemon')
print(', '.join(fruits))

fruits.pop(3)
print(', '.join(fruits))
fruits.remove('banana')
print(', '.join(fruits))
fruits.clear()
print(len(fruits)) # 0

fruits = ['apple', 'kiwi', 'mango', 'apple']
print(fruits.count('apple')) # 2
print(fruits.count('banana')) # 0

fruits_copy = fruits.copy()
fruits_copy.append('mandarin')
print(', '.join(fruits_copy))
print(', '.join(fruits))

kiwi_index = fruits.index('kiwi')
# banana_index = fruits.index('banana') # помилка
apple_index = fruits.index('apple')
print(kiwi_index) # 1
print(apple_index) # 0 - перший знайдений елемент

fruits.sort()
print(', '.join(fruits))
fruits.reverse()
print(', '.join(fruits))

if 'apple' in fruits:
    print('Яблуко в списку!')

list1 = [1, 3, 5]
list2 = [4, 5, 6]
list_concat = list1 + list2
print(list_concat)

list_multiply = list1 * 3
print(list_multiply)

# newlist = [expression for item in iterable if condition == True]

numbers = [0, 3, 4, 3, 5, 6, 4, 5, 3]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

range_list = [x for x in range(4, 13)]
print(range_list)

list2d = [[1,2,3], [4,5,6]]
for l in list2d:
    for i in l:
        print(i, end=' ')
    print()

fruits_tuple = tuple(fruits)
numbers_tuple = ([0, 5, 3, 4])

print(fruits_tuple)
print(numbers_tuple)
print(type(fruits_tuple))

colors = ('red', 'green', 'blue')

(red, green, blue) = colors

colors = ('red', 'green', 'blue', 'yellow', 'pink')

(red, green, blue, *other) = colors
print(type(other))