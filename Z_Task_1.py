#  Створити програму, яка на вхід приймає рядок, та виділяє з нього всі
#  числа в окремий масив, після чого програма друкує рядок без чисел і
#  масив чисел. Змінити цей рядок таким чином, щоб кожне слово в ньому,
#  починалось і закінчувалось великою літерою. Знайти максимальне
#  значення в масиві чисел, а всі інші числа піднести до степеню по їх
#  індексу, та записати в інший масив.

'''
Программа корректно выводит только слова и числа с пробелами, не учитывая остальные символы.
`hi.` - игнор, `hi .` - добавляет в список `hi`. С числами тоже самое.

Я пробовал реализовать выводы с помощью re.findall (в таком случае вышеупомянутая проблема фиксилась), но отказался от этой идеи, так как не смог убрать пустые пробелы при выводе строки без чисел.
'''

# Функция для вывода каждого слова с первой и последней большой буквой строки без чисел


def cap(point):
    if len(point) == 1:
        return point.upper()
    first, *rest, last = point
    return first.upper() + "".join(rest) + last.upper()


# Ввод строки
random_list = input("\n\tEnter any sentence: ")

# Строка без чисел
delete_digits = random_list.split()
words_list = [str(j) for j in filter(
    lambda words: words.isalpha(), delete_digits)]
print("\n\tThe words:\n<> ***", words_list)

# Строка без слов
delete_words = random_list.split()
numbers_list = [int(i) for i in filter(
    lambda numbers: numbers.isnumeric(), delete_words)]
print("\n\tThe digits:\n<> ***", numbers_list)

# Вывод каждого слова с первой и последней большой буквой строки без чисел
capital_letters = words_list
new_words_list = " ".join(map(cap, capital_letters))
print("\n\tThe words with first and last capital letters:\n<> ***", new_words_list)

for i in numbers_list:
    if i == max(numbers_list):
    
        # Максимальное значение в строке без слов
         print("\n\tThe max digit:\n<> ***", max(numbers_list))
         
         # Возведение каждого, кроме максимального, элемента строки без слов в степень за их индексами
         new_list = [x**i for i, x in enumerate(numbers_list) if x != max(numbers_list)]
         print("\n\tOther elements raised to a power by their indices:\n<> ***", new_list, "\n")