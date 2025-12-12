# Винятки

operators = ['+', '-', '*', '/']

while(True):
    try:
        num1 = float(input("Введіть перше число: ").replace(',', '.'))
        num2 = float(input("Введіть друге число: ").replace(',', '.'))

        operator = input("Введіть символ операції (+, -, *, /): ")

        if operator not in operators:
            raise Exception(operator)

        match operator:
            case "+":
                print(f"{num1} + {num2} = {num1 + num2}")
            case "-":
                print(f"{num1} - {num2} = {num1 - num2}")
            case "*":
                print(f"{num1} * {num2} = {num1 * num2}")
            case "/":
                print(f"{num1} / {num2} = {num1 / num2}")
    except ZeroDivisionError:
        print("Не можна ділити на нуль!")
    except ValueError:
        print("Некоректне число!")
    except Exception as ex:
        print(f"Некоректна операція - {ex.args[0]}!")
    finally:
        repeat = input("Повторити? Y/N")
        if repeat == 'N':
            break
