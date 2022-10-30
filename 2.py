# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 

#     1+2*3 => 7; 

#     (1+2)*3 => 9;
# 
from random import choice
from operator import add, sub, mul, truediv


def switcher(op):
    '''
    Декоратор для вычитания и деления
    Выполняет сравнение операндов и перестановку
    Первый операнд >= второй операнд
    '''
    def wrapper(a, b):
        no_switch = a >= b
        try:
            return (op(a, b), False) if no_switch else (op(b, a), True)
        except ZeroDivisionError:
            # При делении на ноль возвращается None
            return None, not no_switch
    return wrapper


def noop_wrap(op):
    '''
    Пустой декоратор для умножения и сложения
    Просто добавляет один возвращаемый параметр False,
    обозначающий, что операнды не меняются местами
    '''
    def wrapper(*args):
        return op(*args), False
    return wrapper


def pair_generator():
    pool = range(10)
    return choice(pool), choice(pool)


def q_generator():
    pair = pair_generator()

    # случайный оператор - случайный ключ словаря
    op = choice(tuple(operations.keys()))

    # результат математического выражения и признак смены местами операндов
    res, switch_flag = operations.get(op)(*pair)

    return '{0} {2} {1} = {3}'.format(*(pair if not switch_flag else reversed(pair)), op, res)


 # карта связей "символ - оператор" с соответствующими обертками
operations = {'+': noop_wrap(add), '-': switcher(sub), '*': noop_wrap(mul), '/': switcher(truediv)}


for _ in range(5):
    print(q_generator())