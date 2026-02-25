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


def print_greeting_with_name(name: str = 'guest') -> None: # name - параметр
    print('============================')
    print(f'==== GREETINGS, {name.upper()}! ====')
    print('============================')


name = input('Enter your name: ')
print_greeting_with_name(name) # name - аргумент


def my_sum(num1: float, num2: float) -> float:
    return num1 + num2


print(my_sum(10.5, 12.4))
print(my_sum(15.5, -2.9))


def print_full_name(first_name: str, last_name: str):
    print(f'{last_name} {first_name}')


print_full_name(last_name='Беккєр', first_name='Володимир')
print_full_name('Володимир', 'Беккєр')


def my_animal(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)


my_animal("dog", name = "Buddy", age = 5)


def only_positional(name, /): # тільки позиційні аргументи
    print("Hello", name)

def only_keyword(*, name): # тільки іменовані аргументи
    print("Hello", name)


def sum_args(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

sum_args(10, 54, 43)
sum_args(10, 87, -9, 0, 76)


def print_kwargs(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

print_kwargs(name = "Tobias", age = 30, city = "Bergen")


def args_kwargs(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

args_kwargs("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def unpack_list(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = unpack_list(*numbers)
print(result)

def upack_dict(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
upack_dict(**person)

def local(local_param):
    local_var = 10 # локальна область видимості
    print(local_param, local_var)

# print(local_var) # Помилка - local_var не доступна

global_var = 10

def global_example():
    print(global_var) # Доступно - global_var доступна в усьому файлі


def enclosing(enclosing_param):
    enclosing_var = 10
    def inner(inner_param):
        inner_var = 11
        print(enclosing_var) # Доступна - enclosing_var доступна у внутрішній функції


var = 10

def func():
    global var # глобальна var
    var = 11
    print(var)

func()

print(var)