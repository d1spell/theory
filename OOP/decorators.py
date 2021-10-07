def counter_add(start):
    def step():
        nonlocal start
        start += 5
        return start

    return step


k = 7
cnt = counter_add(k)
print(cnt())


def counter_add(n):
    def step(star):
        nonlocal n
        star += n
        return star

    return step


# k = int(input())
# cnt = counter_add(2)
# print(cnt(k))

def sorted_list(func):
    def wrapper(*args):
        lst = sorted(func(*args))
        print(*lst)

    return wrapper


@sorted_list
def get_list(string):
    return [int(i) for i in string.split()]


s = '8 11 -5 4 3 10'

get_list(s)

l1 = 'house river tree car'
l2 = 'дом река дерево машина'


def sorted_dict(func):
    def wrapper(*args):
        return dict(zip(*func(*args)))

    return wrapper


@sorted_dict
def convert(*args):
    return args[0].split(), args[1].split()


d = convert(l1, l2)
print(*sorted(d.items()))

import re

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

string = 'Python - это круто!'
string.replace(': ;.,_', '-')
print(string)


def translator(func):
    def wrapper(*args):
        return re.sub(r'-+', '-', func(*args))

    return wrapper


def trans(string):
    string = re.sub(r'[: ;_.,]', '-', string).lower()
    return ''.join([t[i] if i in t else i for i in string])


print(trans(string))
print(translator(trans)(string))

from functools import wraps


def decor(func):
    @wraps(func)
    def wrapper(*args):
        return sum(func(*args))

    return wrapper


@decor
def get_list(string):
    """Функция для формирования списка целых значений"""
    return [int(i) for i in string.split()]


print(get_list("1 2 3 -1 -2 -3"))

with open('../123.txt', encoding='utf-8') as f:
    a = f. readlines()
    f.seek(0)
    b = f.readline()
    b1 = f.readline()
    f.seek(0)
    c = f.read(40)

print(a)
print(b)
print(b1)

print(c)
