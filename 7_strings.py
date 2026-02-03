text = "Hello, world!"

print(text[0]) # H
print(text[7]) # w

#print(text[22]) # Помилка!

print(text[:10])    # Hello, wor
print(text[3:6])    # lo,
print(text[3:])     # lo, world!
print(text[3:10:4]) # lw
print(text[::2])    # Hlo ol!

print(text[-1]) # !
print(text[-4]) # r

print(text[::-1])       # !dlrow ,olleH
print(text[:-7:-1])     # !dlrow
print(text[-3:-10:-1])  # lrow ,o

# text[5] = "U" # помилка

print(len(text)) # 13

counter = 0
while counter < len(text):
    print(text[counter], end=', ')
    counter += 1

print()

for i in text:
    print(i, end=', ')

print()

text_upper = text.upper()
text_lower = text.lower()
print(text_upper) # всі великі
print(text_lower) # всі маленькі
print(text) # оригінальний рядок не змінився!

text = "   Hello, world!    "
text_stripped = text.strip()
print(text_stripped)
print(text) # Не змінився!

text = text_stripped

text_modified = text.replace('l', 'P')
text_modified2 = text.replace('world', 'python')
print(text_modified)
print(text_modified2)

splitted = text.split(', ')
print(splitted)

part1 = 'Hello'
part2 = 'Python'

concat = part1 + ', ' + part2 + '!'
print(concat)

symbol = '*'
print(symbol * 8)

if 'a' in 'apple':
    print('a in apple')

if 'Hello' in concat:
    print('Hello in concat')

if text.startswith('Hello'):
    print('this is greeting')

if text.endswith('!'):
    print('this is exclamation')

fruit = input('Enter fruit name: ')
if fruit == 'apple':
    print('fruit is an apple')

print('lemon' > 'apple') # True
print('green' < 'blue') # False


message = 'Hello, Unicode!'

encoded = message.encode("utf-16")
print(encoded)

decoded = encoded.decode("utf-16")
print(decoded)
