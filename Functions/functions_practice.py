'''
Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. 
Межі діапазону передаються як параметри. 
Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.
'''

def range_multiply(left, right):
    if left > right:
        left, right = right, left
    result = 1
    for i in range(left, right + 1):
        result *= i
    return result

print(range_multiply(10, 13))
print(range_multiply(12, 5))