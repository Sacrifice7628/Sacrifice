:postal_horn: **Условие:**

  Створити програму, яка на вхід приймає рядок, та виділяє з нього всі числа в окремий масив, після чого програма друкує рядок без чисел і масив чисел. Змінити цей рядок таким чином, щоб кожне слово в ньому, починалось і закінчувалось великою літерою. Знайти максимальне значення в масиві чисел, а всі інші числа піднести до степеню по їх індексу, та записати в інший масив.
  
:yo_yo: **От автора:**

  Программа корректно выводит только слова и числа с пробелами, не учитывая остальные символы.
`hi.` - игнор, `hi .` - добавляет в список `hi`. С числами тоже самое.

![fail](https://user-images.githubusercontent.com/86672075/124384806-ae96d080-dcdb-11eb-82a8-167691ac1d18.png)

  Я пробовал реализовать выводы с помощью `re.findall` (в таком случае вышеупомянутая проблема фиксилась), но отказался от этой идеи, так как не смог убрать пустые пробелы при выводе строки без чисел.
 
 :jigsaw: **Комментарии к коду:**
 
### Функция для вывода каждого слова с первой и последней большой буквой строки без чисел
```python
def cap(point):
    if len(point) == 1:
        return point.upper()
    first, *rest, last = point
    return first.upper() + "".join(rest) + last.upper()
```

### Ввод строки
```python
random_list = input("\n\tEnter any sentence: ")
```

### Строка без чисел
```python
delete_digits = random_list.split()
words_list = [str(j) for j in filter(
    lambda words: words.isalpha(), delete_digits)]
print("\n\tThe words:\n<> ***", words_list)
```

### Строка без слов
```python
delete_words = random_list.split()
numbers_list = [int(i) for i in filter(
    lambda numbers: numbers.isnumeric(), delete_words)]
print("\n\tThe digits:\n<> ***", numbers_list)
```

### Вывод каждого слова с первой и последней большой буквой строки без чисел
```python
capital_letters = words_list
new_words_list = " ".join(map(cap, capital_letters))
print("\n\tThe words with first and last capital letters:\n<> ***", new_words_list)
```

### Максимальное значение в строке без слов
```python
print("\n\tThe max digit:\n<> ***", max(numbers_list))
```

### Возведение каждого, кроме максимального, элемента строки без слов в степень за их индексами
```python
new_list = [x**i for i, x in enumerate(numbers_list) if x != max(numbers_list)]
print("\n\tOther elements raised to a power by their indices:\n<> ***", new_list, "\n")
```

:game_die: **Результат:**

![result](https://user-images.githubusercontent.com/86672075/124384791-9cb52d80-dcdb-11eb-9008-8314219f4799.png)

:pager: **Работа с Git Bash:**

- открываем репозиторий

![git_bash](https://user-images.githubusercontent.com/86672075/124385237-9627b580-dcdd-11eb-8a05-01fe75a6e6fc.jpg)

- коммитим и пушим Task_1

![git_bash_1](https://user-images.githubusercontent.com/86672075/124385381-f4549880-dcdd-11eb-9d1e-b82545b7d377.jpg)
