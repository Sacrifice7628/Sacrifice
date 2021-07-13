from tkinter import *
from math import *
import math
import numpy as np

input = ''


# Функция для различных математических действий


def sign(smth):

    global input

    input = input + str(smth)
    equation.set(input)


# Функция для результата


def equalsign():

    try:
        global input
        input = input.replace('ln', 'np.log')
        total = str(eval(input))
        equation.set(total)

        input = ''

    except:
        equation.set(' Error ')
        input = ''


# Функция для полной очистки поля


def clear():

    global input
    input = ''
    equation.set('0')


# Функция для удаления одного символа


def delete():
    global input
    text = input[:-1]
    input = text
    equation.set(text)


# Функция для квадратного корня из числа


def sqrt():
    global input
    input = math.sqrt(eval(input))
    equation.set(float(input))
    input = eval(input)


# Функции для факториала


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


def factorial_func():
    global input
    result = str(factorial(eval(input)))
    input = result
    equation.set(result)


# Функция для нахождения процента


def percent():
    global input
    point = str(eval(input+'/100'))
    input = point
    equation.set(point)


# Функция для синуса


def sin():
    global input
    point = str(math.sin(math.radians(eval(input))))
    input = point
    equation.set(point)


#  Функция для косинуса


def cos():
    global input
    point = str(math.cos(math.radians(eval(input))))
    input = point
    equation.set(point)


#  Функция для тангенса


def tan():
    global input
    point = str(math.tan(math.radians(eval(input))))
    input = point
    equation.set(point)


# Функция для котангенса


def ctg():
    global input
    point = str(1/math.tan(math.radians(eval(input))))
    input = point
    equation.set(point)


window = Tk()
# Заголовок окна
window.title("Calculator")
# Размер окна
window.geometry('355x750')
# Цвет заднего фона окна
window.configure(bg='#80bfff')
# Иконка перед заголовком окна
window.iconbitmap('Icons/calculator_icon.ico')
# Запрет на изменение размера окна
window.resizable(False, False)

# Добавление строки с вводом справа налево, поле и его параметры
button_frame = Frame(window, bg='#80bfff')
button_frame.pack()
equation = StringVar()
equation.set('0')
input_field = Entry(button_frame, textvariable=equation,
                    justify='right', font=('arial', 20, 'bold'))
input_field.pack()
input_field.grid(row=0, column=0, ipadx=8, columnspan=4, ipady=25, pady=15)

# Создаём кнопки, задавая им параметры (шрифт, размер шрифта, название, контур, рельеф фона, цвет названия, цвет фона, ширину и высоту кнопки) и месторасположение (номер ряда и столбца)

'''C'''

button_clear = Button(button_frame, font=('times new roman', 12), text='C', bd=1, relief='ridge',
                      fg='black', bg='white', command=clear, height=3, width=8)
button_clear.grid(row=1, column=0)

'''Del'''

button_delete = Button(button_frame, font=('times new roman', 12), text='Del', bd=1, relief='ridge',
                       fg='black', bg='white', command=delete, height=3, width=8)
button_delete.grid(row=1, column=1)

'''√'''

button_sqrt = Button(button_frame, font=('times new roman', 12), text='\u00B2\u221A', bd=1, relief='ridge',
                     fg='black', bg='white', command=sqrt, height=3, width=8)
button_sqrt.grid(row=1, column=2)

'''x^n'''

button_power = Button(button_frame, font=('times new roman', 12), text='x^n', bd=1, relief='ridge',
                      fg='black', bg='white', command=lambda: sign('**'), height=3, width=8)
button_power.grid(row=1, column=3)

'''/'''

button_divide = Button(button_frame, font=('times new roman', 12), text='/', bd=1, relief='ridge',
                       fg='black', bg='white', command=lambda: sign("/"), height=3, width=8)
button_divide.grid(row=2, column=3)

'''7'''

button_7 = Button(button_frame, font=('times new roman', 12), text='7', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(7), height=3, width=8)
button_7.grid(row=2, column=0)

'''8'''

button_8 = Button(button_frame, font=('times new roman', 12), text='8', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(8), height=3, width=8)
button_8.grid(row=2, column=1)

'''9'''

button_9 = Button(button_frame, font=('times new roman', 12), text='9', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(9), height=3, width=8)
button_9.grid(row=2, column=2)

'''*'''

button_multiply = Button(button_frame, font=('times new roman', 12), text='*', bd=1, relief='ridge',
                         fg='black', bg='white', command=lambda: sign("*"), height=3, width=8)
button_multiply.grid(row=3, column=3)

'''4'''

button_4 = Button(button_frame, font=('times new roman', 12), text='4', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(4), height=3, width=8)
button_4.grid(row=3, column=0)

'''5'''

button_5 = Button(button_frame, font=('times new roman', 12), text='5', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(5), height=3, width=8)
button_5.grid(row=3, column=1)

'''6'''

button_6 = Button(button_frame, font=('times new roman', 12), text='6', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(6), height=3, width=8)
button_6.grid(row=3, column=2)

'''-'''
button_minus = Button(button_frame, font=('times new roman', 12), text='-', bd=1, relief='ridge',
                      fg='black', bg='white', command=lambda: sign("-"), height=3, width=8)
button_minus.grid(row=4, column=3)

'''1'''

button_1 = Button(button_frame, font=('times new roman', 12), text='1', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(1), height=3, width=8)
button_1.grid(row=4, column=0)

'''2'''

button_2 = Button(button_frame, font=('times new roman', 12), text='2', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(2), height=3, width=8)
button_2.grid(row=4, column=1)

'''3'''

button_3 = Button(button_frame, font=('times new roman', 12), text='3', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(3), height=3, width=8)
button_3.grid(row=4, column=2)

'''+'''

plus = Button(button_frame, font=('times new roman', 12), text='+', bd=1, relief='ridge',
              fg='black', bg='white', command=lambda: sign("+"), height=3, width=8)
plus.grid(row=5, column=3)

'''π'''

button_more = Button(button_frame, font=('times new roman', 12), text='π', bd=1, relief='ridge',
                     fg='black', bg='white', command=lambda: sign(str(math.pi)), height=3, width=8)
button_more.grid(row=5, column=0)

'''0'''

button_0 = Button(button_frame, font=('times new roman', 12), text='0', bd=1, relief='ridge',
                  fg='black', bg='#d6ecff', command=lambda: sign(0), height=3, width=8)
button_0.grid(row=5, column=1)

'''.'''

button_decimal = Button(button_frame, font=('times new roman', 12), text='.', bd=1, relief='ridge',
                        fg='black', bg='white', command=lambda: sign('.'), height=3, width=8)
button_decimal.grid(row=5, column=2)

'''='''

button_equal = Button(button_frame, font=('times new roman', 12), text=' = ', bd=0, relief='groove',
                      fg='#0039e6', bg='#d4d5d7', command=equalsign, height=3)
button_equal.grid(row=6, column=0, columnspan=4, sticky='nwse')

'''n!'''

button_factorial = Button(button_frame, font=('times new roman', 12), text='n!', bd=1, relief='ridge',
                          fg='black', bg='white', command=factorial_func, height=3, width=8)
button_factorial.grid(row=7, column=0)

'''%'''

button_percent = Button(button_frame, font=('times new roman', 12), text='%', bd=1, relief='ridge',
                        fg='black', bg='white', command=percent, height=3, width=8)
button_percent.grid(row=7, column=1)

'''('''

button_power = Button(button_frame, font=('times new roman', 12), text='(', bd=1, relief='ridge',
                      fg='black', bg='white', command=lambda: sign('('), height=3, width=8)
button_power.grid(row=7, column=2)

''')'''

button_power = Button(button_frame, font=('times new roman', 12), text=')', bd=1, relief='ridge',
                      fg='black', bg='white', command=lambda: sign(')'), height=3, width=8)
button_power.grid(row=7, column=3)

'''sin'''

button_sin = Button(button_frame, font=('times new roman', 12), text='sin', bd=1, relief='ridge',
                    fg='black', bg='white', command=sin, height=3, width=8)
button_sin.grid(row=8, column=0)

'''cos'''

button_cos = Button(button_frame, font=('times new roman', 12), text='cos', bd=1, relief='ridge',
                    fg='black', bg='white', command=cos, height=3, width=8)
button_cos.grid(row=8, column=1)

'''tan'''

button_tan = Button(button_frame, font=('times new roman', 12), text='tan', bd=1, relief='ridge',
                    fg='black', bg='white', command=tan, height=3, width=8)
button_tan.grid(row=8, column=2)

'''ctg'''

button_ctg = Button(button_frame, font=('times new roman', 12), text='ctg', bd=1, relief='ridge',
                    fg='black', bg='white', command=ctg, height=3, width=8)
button_ctg.grid(row=8, column=3)

'''log'''

button_log = Button(button_frame, font=('times new roman', 12), text='log\u2081\u2080', bd=1, relief='ridge',
                    fg='black', bg='white', command=lambda: sign('log10('), height=3, width=8)
button_log.grid(row=9, column=0)

'''ln'''

button_ln = Button(button_frame, font=('times new roman', 12), text='ln', bd=1, relief='ridge',
                   fg='black', bg='white', command=lambda: sign('ln('), height=3, width=8)
button_ln.grid(row=9, column=1)

'''abs'''

button_cub = Button(button_frame, font=('times new roman', 12), text='abs', bd=1, relief='ridge',
                    fg='black', bg='white', command=lambda: sign('abs('), height=3, width=8)
button_cub.grid(row=9, column=2)

'''bin'''

button_bin = Button(button_frame, font=('times new roman', 12), text='bin', bd=1, relief='ridge',
                    fg='black', bg='white', command=lambda: sign('bin('), height=3, width=8)
button_bin.grid(row=9, column=3)


window.mainloop()
