a = 10
b = 12
if b > a: print('b більше за a')

a = 2
b = 330
print("A") if a > b else print("B")

a = 12
b = 10
print('A') if a > b else print('==') if b == a else print('B')

# Встановлення значення за замовчуванням
username = input("Введіть ваш логін: ")
display_name = username if username else "Гість"
print('Привіт,', display_name)

age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

# Конструкція match-case

'''
match <змінна або вираз>:
    case <значення1>:
        інструкція 1
        інструкція 2
    case <значення2>:
        інструкція 1
        ...
    ...
'''

day = 4

if day == 1:
  print('Понеділок')
elif day == 2:
  print('Вівторок')
elif day == 3:
  print('Середа')
elif day == 4:
  print('Четвер')
elif day == 5:
  print('П\'ятниця')
elif day == 6:
  print('Субота')
elif day == 7:
  print('Неділя')

match day:
  case 1: print('Понеділок')
  case 2: print('Вівторок')
  case 3: print('Середа')
  case 4: print('Четвер')
  case 5: print('П\'ятниця')
  case 6: print('Субота')
  case 7: print('Неділя')
  case _: print('Неправильний номер дня!')

month = 3

match month:
  case 12 | 1 | 2: print('Зима')
  case 3 | 4 | 5: print('Весна')
  case 6 | 7 | 8: print('Літо')
  case 9 | 10 | 11: print('Осінь')

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("Будній день в квітні")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("Будній день в травні")