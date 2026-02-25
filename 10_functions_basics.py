contacts = {
    'Аня': {
        'мобільний': '0506059596',
        'робочий': None
    },
    'Антон СТО': {
        'мобільний': None,
        'робочий': '0650600069'
    },
    'Тимофій Карпати': {
        'мобільний': '0506059596',
        'робочий': '0769998868'
    }
}

def print_contact(contact):
    if contact['мобільний'] != None: print(f"Мобільний: {contact['мобільний']}") 
    if contact['робочий'] != None: print(f"Робочий: {contact['робочий']}")

choice = int(input("1. Знайти контакт\n2. Вивести всі контакти\n0. Вихід\nОберіть дію:"))

while choice != 0:
    match choice:
        case 1:
            name = input("Введіть ім'я контакту: ")
            if name in contacts:
                print_contact(contacts[name])
                # print(f"Мобільний: {contacts[name]['мобільний']}")
                # print(f"Робочий: {contacts[name]['робочий']}")
            else:
                print("Немає такого контакту")
        case 2:
            for contact in contacts:
                print(f"{contact}:")
                print_contact(contacts[name])
                # print(f"Мобільний: {contacts[contact]['мобільний']}")
                # print(f"Робочий: {contacts[contact]['робочий']}")
        case _: print("Нема такого варіанту!")

    choice = input("1. Знайти контакт\n2. Вивести всі контакти\n0. Вихід\nОберіть дію:")

'''
def назва_функці(параметр1, параметр2...):
    інструкція1
    інструкція2
    ...
'''

def print_greeting():
    print('============================')
    print('==== GREETINGS, FRIEND! ====')
    print('============================')


def print_greeting_with_name(name: str): # name - параметр
    print('============================')
    print(f'==== GREETINGS, {name.upper()}! ====')
    print('============================')


name = input('Enter your name: ')
print_greeting_with_name(name) # name - аргумент


def my_sum(num1: float, num2: float):
    return num1 + num2


print(my_sum(10.5, 12.4))
print(my_sum(15.5, -2.9))