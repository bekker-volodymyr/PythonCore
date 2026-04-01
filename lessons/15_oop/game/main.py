from enemies import *
from players import *

# Створюємо об'єкти
grob = Goblin("Grob", 10, 30)
vlad = Vampire("Vlad", 12, 40)
boris = Fighter("Boris", 15, 50)
anna = Healer("Anna", 8, 35)

print("--- Початковий стан ---")
print(grob, vlad, boris, anna, sep="\n")
print("-" * 30)

# Раунд 1: Гоблін і Вампір атакують бійця
grob.attack(boris)
vlad.suck_blood(boris)

# Раунд 2: Боєць відповідає Гобліну, Цілитель лікує Бійця
boris.attack(grob)
anna.heal(boris)

# Раунд 3: Вампір атакує Цілителя
vlad.attack(anna)

print("\n--- Стан після сутички ---")
print(grob, vlad, boris, anna, sep="\n")