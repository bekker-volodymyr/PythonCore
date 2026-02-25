'''
Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. 
Межі діапазону передаються як параметри. 
Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.
'''

def range_multiply(left: int, right: int) -> int:
    if left > right: 
        left, right = right, left
    result = 1
    for i in range(left, right):
        result *= i
    return result
    