# Сформувати список із 30 випадкових цілих чисел від -100 до +100.
# Знайти максимальний елемент списку і його порядковий номер. Вивести пари від’ємних чисел, що стоять поруч.

import random

# Сформований список із 30 випадкових цілих чисел від -100 до +100.
print("\n\nA list of 30 random integers from -100 to +100:")
array = range(-100, 100)
numbers = random.sample(array, 30)
print(numbers)

# Максимальний елемент списку.
print("\nMaximum list item:")
print(max(numbers))

# Порядковий номер максимального елементу списку.
print("\nSequence number of the maximum list item:")
print(numbers.index(max(numbers)))

# Пари від’ємних чисел, що стоять поруч.
print("\nPairs of negative numbers standing side by side:\n")
for i in range(len(numbers)-1):
    if numbers[i] < 0 and numbers[i+1] < 0:
        print(numbers[i], numbers[i+1])
