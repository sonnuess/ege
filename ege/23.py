a = 2
b = 128

def f(x):
    if x == 128:
        global c
        c += 1
    if x < 128:
        f(x+5)
        f(x+8)

c = 0
f(a)
print(c)

#135120
"""
Исполнитель преобразует число, записанное на экране.
У исполнителя есть команды, которым присвоены номера:
Прибавить 1,
Прибавить 4,
Умножить на 4

Первая команда увеличивает число на экране на 1, вторая — на 4, третья — увеличивает число в 4 раза.
Сколько существует программ, для которых при исходном числе 3 результатом является число 27 и при этом траектория содержит число 11?
"""
a = 3
b = 27

def f(x, prev):
    global c
    if x == 27 and 11 in prev:
        c += 1
    if x < 27:
        prev.append(x)
        f(x+1, prev[:])
        f(x+4, prev[:])
        f(x*4, prev[:])

c = 0
f(a, [])
print(c)









'''
Исполнитель Калькулятор преобразует число на экране.
У исполнителя есть три команды, которым присвоены номера:

Прибавить 1
Умножить на 2
Прибавить 3

Первая команда увеличивает число на экране на 1, вторая умножает его на 2, третья увеличивает на 3.

Программа для исполнителя Калькулятор — это последовательность команд.

Сколько существует программ, которые преобразуют исходное число 2 в число 20 и при этом траектория вычислений не содержит чисел 7 и 15?
'''
a = 2
b = 20
def f(x, prev):
    global c
    if x == 20 and 7 not in prev and 15 not in prev:
        c += 1

    if x < 20:
        prev.append(x)
        f(x+1, prev[:])
        f(x*2, prev[:])
        f(x+3, prev[:])

c = 0
f(a, [])
print(c)

# 304

'''
Вычесть 3
Поделить на 3  , если число кратно 3
Поделить на 2  , если число кратно 2
Программа для исполнителя — это последовательность команд.

Сколько существует программ, для которых при исходном числe 30   результатом является число 3  ?
'''

a = 30
b = 3
def f(x):
    global c
    if x == 3 :
        c += 1

    if x > 3:
        f(x-3)
        if x % 3 == 0:
            f(x/3)
        if x % 2 == 0:
            f(x/2)


c = 0
f(a)
print(c)

# 23

'''
У исполнителя есть три команды:
Вычесть 3
Вычесть 1
Поделить на 2  , если число четное

Программа для исполнителя — это последовательность команд.

Сколько существует программ, для которых при исходном числe 33   результатом является число 12  , при этом программа содержит 9   команд?
'''

a = 33
b = 12
def f(x, prev):
    global c
    if x == 12 and (len(prev) == 9):
        c += 1
    elif x > 12:
        prev.append(x)
        f(x-3, prev[:])
        f(x-1, prev[:])
        if x % 2 == 0:
            f(x/2, prev[:])


c = 0
f(a, [])
print(c)

# 85










'''
Прибавь 1,

Раздели на 2.

Первая из них увеличивает число на экране на 1,   вторую же можно применять только для четных чисел, и она делит его на 2.

Программа для Хитрителя — это последовательность команд. Сколько есть программ, которые применяют вторую команду не более 4   раз и преобразуют число 10   в число 20  ?
'''

a = 10
b = 20
def f(x, prev, c2=4):
    global c
    if x == 20 and c2 >= 0:
        c += 1
        print(prev)
    elif x < 20 and c2 >= 0:
        prev.append(x)
        f(x+1, prev[:], c2)
        if x % 2 == 0:
            f(x//2, prev[:], c2-1)



c = 0
f(a, [])
print(c)

# 1591



'''
У исполнителя Калькулятор имеются три команды, которым присвоены номера:
Вычесть 1
Вычесть 3
Найти целую часть от деления на 2
Выполняя первую из них, исполнитель уменьшает число на экране на 1, выполняя вторую – уменьшает на 3, выполняя третью – делит на 2 нацело, отбрасывая остаток.
 Сколько существует программ, для которых при исходном числе 19 результатом является число 3, и при этом траектория вычислений содержит число 10 и не содержит числа 7?
'''

a = 19
b = 3
def f(x, prev):
    global c
    if x == 3 and (10 in prev) and (7 not in prev):
        c += 1
      #  print(prev)
    elif x > 3 :
        prev.append(x)
        f(x-1, prev[:])
        f(x-3, prev[:])
        f(x//2, prev[:])
c = 0
f(a, [])
print(c)

#133

a = 2
b = 25
def f(x):
    global c
    if x == 25:
        c += 1
    if x < 25:
        f(x+1)
        f(x+2)
        f(x*4)
c = 0
f(a)
print(c)
#49468


'''
task
'''
a = 2
b = 13

def f(x, prev):
    global c
    if x == 13 and 10 in prev:
        c += 1
    elif x < 13:
        prev.append(x)
        f(x+1, prev[:])
        f(x+2, prev[:])
        f(x*2, prev[:])

c = 0
f(a, [])
print(c)


a = 2
b = 27

def f(x, prev):
    global c
    if x == 27 and 13 in prev and 19 in prev:
        c += 1
    elif x < 27:
        prev.append(x)
        f(x+1, prev[:])
        f(x+2, prev[:])
        f(x*2, prev[:])
        f(x*3, prev[:])
c = 0
f(a, [])
print(c)

''' task '''
a = 2
b = 20

def f(x, prev):
    global c
    if x == 20 and 7 not in prev and 15 not in prev:
        c += 1
    elif x < 20:
        prev.append(x)
        f(x+1, prev[:])
        f(x*2, prev[:])
        f(x+3, prev[:])
c = 0
f(a, [])
print(c)

a = 1
b = 10
def f(x):
    global c
    if x == 10:
        c += 1
    elif x < 10:
        f(x+1)
        f(x+2)
        f(x+x-1)

c = 0
f(1)
print(c)


'''
Исполнитель преобразует целое число, записанное на экране.

У исполнителя две команды, которым присвоены номера:
преобразует целое число, записанное на экране.
1. Прибавить 1,
2. Прибавить 2,
3. Прибавить предыдущее.
Первая команда увеличивает число на экране на 1, вторая увеличивает это число на 2,
третья прибавляет к числу на экране число, меньшее на 1
(к числу 3 прибавляется 2, к числу 11 прибавляется 10 и т. д.).
Программа для исполнителя М.Е.М.249 – это последовательность команд.
Сколько существует программ, которые число 1 преобразуют в число 10?
'''
import sys

sys.setrecursionlimit(1000)

a = 1
b = 10
def f(x):
    global c
    if x == 10:
        c += 1
    elif x < 10:
        f(x+1)
        f(x+2)
        if x != 1:
           f(x+x-1)

c = 0
f(1)
print(c)


def f(x, prev):
    global cnt
    if (x == 3) and (9 not in prev) and (16 not in prev):
        cnt += 1
    elif x > 3:
        prev.append(x)
        f(x-1, prev[:])
        f(x-2, prev[:])
        f(x//3, prev[:])
cnt = 0
f(19, [])
print(cnt)


def f(x, prev):
    global cnt
    if (x == 15) and (8 in prev) and (10 in prev):
        cnt += 1
    elif x < 15:
        prev.append(x)
        f(x+1, prev[:])
        f(x*2, prev[:])


cnt = 0
f(4, [])
print(cnt)
