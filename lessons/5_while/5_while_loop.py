'''
while <умова>:
    інструкція 1
    інструкція 2
    інструкція 3
    ...
'''

# Чистка картоплі

'''
need_potatoes = 4

peeled_potatoes = 0
print('Чистимо картоплю...')
print('Готово!')
peeled_potatoes += 1
print('Чистимо картоплю...')
print('Готово!')
peeled_potatoes += 1
print('Чистимо картоплю...')
print('Готово!')
peeled_potatoes += 1
print('Чистимо картоплю...')
print('Готово!')
peeled_potatoes += 1
'''

need_potatoes = int(input("Скільки потрібно картоплі: "))

peeled_potatoes = 0

while peeled_potatoes < need_potatoes:
    print('Чистимо картоплю...')
    print('Готово!')
    peeled_potatoes += 1

while True:
    num1 = float(input('Введіть перше число: '))
    num2 = float(input('Введіть друге число: '))
    action = input('Введіть операцію (+, -, *, /):')
    match action:
        case '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        case '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        case '*':
            print(f'{num1} * {num2} = {num1 * num2}')
        case '/':
            if num2 == 0:
                print('Не можна ділити на 0!')
            else:
                print(f'{num1} / {num2} = {num1 / num2}')
    quit = input('Введіть q щоб завершити роботи або Enter щоб продовжити')
    if quit == 'q':
        break


while peeled_potatoes < need_potatoes:
    print('Беремо картоплю...')
    is_rotten = input('Ця картопля хороша чи гнила?')
    if is_rotten == 'гнила':
        print('Викидаємо картоплю та переходимо до наступної')
        continue
    print('Чистимо картоплю...')
    print('Готово!')
    peeled_potatoes += 1
    is_tired = input('Ви втомились?')
    if is_tired == 'так':
        break
else:
    print('Картопля почищена!')