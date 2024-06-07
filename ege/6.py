'''
Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат,
её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует три команды: Вперёд n   (где n   — целое число), вызывающая передвижение Черепахи на n   единиц в том направлении, куда указывает её голова, Направо m   (где m   — целое число), вызывающая изменение направления движения на m   градусов по часовой стрелке, и Налево m   (где m   — целое число), вызывающая изменение направления движения на m градусов против часовой стрелки.

Запись Повтори k   [Команда1   Команда2   …КомандаS  ] означает, что последовательность из S   команд повторится k   раз.

Черепахе был дан для исполнения следующий алгоритм:

Налево 90
Повтори 4
    [Повтори 4
        [Повтори 4
            {Вперёд 3   Направо 120}
        Вперёд 3  ]
    Вперёд 3].

Определите количество равносторонних треугольников которые можно найти на полученной фигуре.
'''

import turtle


a = 20

turtle.speed(5)
turtle.pendown()
turtle.left(90*a)

for i in range(0, 4):
    for _ in range(0, 4):
        for k in range(0, 4):
            turtle.forward(3*a)
            turtle.right(120)
        turtle.forward(3*a)
    turtle.forward(3*a)

turtle.done()


'''
Черепахе был дан для исполнения следующий алгоритм:
Повтори 96
    [Направо 45   Вперёд 1   Направо 45   Вперёд 1   Направо 315   Вперёд 1  ].
Определите, из какого количества отрезков будет состоять фигура, заданная данным алгоритмом.
'''

import turtle

a = 70

turtle.speed(50)
turtle.pendown()

for i in range(0, 96):
    turtle.right(45)
    turtle.forward(1*10)
    turtle.right(45)
    turtle.forward(1*a)
    turtle.right(315)
    turtle.forward(1*a)

turtle.done()
#24


"""
Повтори 10   [Повтори 10   [Вперёд 3   Налево 90  ] Направо 90   Вперёд 5  ].
Сколько точек: лежит внутри фигуры (включа или не включая точки на линии)
"""
import turtle

turtle.tracer(0)
k = 20


turtle.penup()
for x in range(-10*k, 10*k, k):
    for y in range(-5*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(5, 'red')

turtle.goto(0, 0)
turtle.pendown()

for i in range(10):
    for j in range(10):
        turtle.forward(3*k)
        turtle.left(90)
    turtle.right(90)
    turtle.forward(5*k)

turtle.done()



"""
Черепахе был дан для исполнения следующий алгоритм:
Повтори 4   [Вперёд 5   Направо 150   Вперёд 5   Направо 30  ].
Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом.
Точки на линии учитывать не следует.
"""
import turtle

turtle.tracer(5)
k = 40

turtle.penup()
for x in range(-10*k, 10*k, k):
    for y in range(-5*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(5, 'red')

turtle.goto(0, 0)
turtle.pendown()
for i in range(4):
    turtle.forward(5*k)
    turtle.right(150)
    turtle.forward(5*k)
    turtle.right(30)

turtle.done()


'''
Повтори 4   [Вперёд 5   Направо 150   Вперёд 5   Направо 30  ].
Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом.
Точки на линии учитывать не следует.
'''


import turtle

turtle.tracer(3)
k = 20

turtle.penup()
for x in range(-10*k, 10*k, k):
    for y in range(-5*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(5, 'red')

turtle.goto(0, 0)
turtle.pendown()

for i in range(4):
    turtle.forward(5*k)
    turtle.right(150)
    turtle.forward(5*k)
    turtle.right(30)

turtle.done()
#10

'''
Повтори 3   [Вперёд 7   Направо 120  ].
Определите, сколько точек с целочисленными координатами будут находиться внутри области,
ограниченной линией, заданной данным алгоритмом.
Точки на линии учитывать не следует.
'''


import turtle

turtle.tracer(3)
k = 20

turtle.penup()
for x in range(-10*k, 10*k, k):
    for y in range(-10*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(5, 'red')

turtle.goto(0, 0)
turtle.pendown()

for i in range(3):
    turtle.forward(7*k)
    turtle.right(120)


turtle.done()
#18

'''
Повтори 7   [Направо 90   Вперёд 4   Повтори 2   [Направо 270   Вперёд 3  ]].
Определите периметр получившейся фигуры.
'''


import turtle

turtle.tracer(3)
k = 20

turtle.penup()
for x in range(-10*k, 10*k, k):
    for y in range(-10*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(5, 'red')

turtle.goto(0, 0)
turtle.pendown()

for i in range(7):
    turtle.right(90)
    turtle.forward(4*k)
    for j in range(2):
        turtle.right(270)
        turtle.forward(3*k)

turtle.done()
#40

'''
Черепахе был дан для исполнения следующий алгоритм:
Повтори 2 [Вперёд 10 Направо 90 Вперёд 18 Направо 90]
Поднять хвост
Вперёд 5 Направо 90 Вперёд 7 Налево 90
Опустить хвост
Повтори 2 [Вперёд 10 Направо 90 Вперёд 7 Направо 90]
Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур,
ограниченных заданными алгоритмом линиями, включая точки на линиях.
'''
import turtle

turtle.tracer(3)
k = 20

turtle.penup()
for x in range(-10*k, 20*k, k):
    for y in range(-30*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(5, 'red')

turtle.goto(0, 0)
turtle.pendown()

for i in range(2):
    turtle.forward(10*k)
    turtle.right(90)
    turtle.forward(18*k)
    turtle.right(90)

turtle.penup()

turtle.forward(5*k)
turtle.right(90)
turtle.forward(7*k)
turtle.left(90)

turtle.pendown()

for j in range(2):
    turtle.forward(10*k)
    turtle.right(90)
    turtle.forward(7*k)
    turtle.right(90)

turtle.done()
#249


'''
Черепахе был дан для исполнения следующий алгоритм:
Повтори 2 [Вперёд 13 Направо 90 Вперёд 20 Направо 90]
Поднять хвост
Вперёд 8 Направо 90 Назад 3 Налево 90
Опустить хвост
Повтори 2 [Вперёд 16 Направо 90 Вперёд 8 Направо 90]
Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур, ограниченного
заданными алгоритмом линиями, включая точки на линиях
'''
import turtle

turtle.tracer(5)
k = 20

turtle.penup()
for x in range(-10*k, 30*k, k):
    for y in range(-30*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(5, 'red')

turtle.goto(0, 0)
turtle.pendown()

for i in range(2):
    turtle.forward(13*k)
    turtle.right(90)
    turtle.forward(20*k)
    turtle.right(90)

turtle.penup()

turtle.forward(8*k)
turtle.right(90)
turtle.back(3*k)
turtle.left(90)

turtle.pendown()

for j in range(2):
    turtle.forward(16*k)
    turtle.right(90)
    turtle.forward(8*k)
    turtle.right(90)

turtle.done()
#411

'''
Черепахе был дан для исполнения следующий алгоритм:

Направо 90
Повтори 3 [Направо 45 Вперёд 10 Направо 45]
Направо 315 Вперёд 10
Повтори 2 [Направо 90 Вперёд 10].

Определите, сколько точек с целочисленными координатами будут находиться внутри области,
которая ограничена линией, заданной алгоритмом.
Точки на линии учитывать не следует.
'''
import turtle

turtle.tracer(5)
k = 20

turtle.penup()
for x in range(-15*k, 15*k, k):
    for y in range(-30*k, 20*k, k):
        turtle.goto(x, y)
        turtle.dot(3, 'red')

turtle.goto(0, 0)
turtle.pendown()

turtle.right(90)
for i in range(3):
    turtle.right(45)
    turtle.forward(10*k)
    turtle.right(45)
turtle.right(315)
turtle.forward(10*k)
for j in range(2):
    turtle.right(90)
    turtle.forward(10*k)

turtle.done()
#203



import turtle as t

k = 20
t.tracer(5)

t.penup()
for x in range(-30*k, 30*k, k):
    for y in range(-40*k, 40*k, k):
        t.goto(x,y)
        t.dot(5, 'purple')
t.goto(0,0)
t.pendown()

for _ in range(2):
    t.forward(13*k)
    t.right(90)
    t.forward(20*k)
    t.forward(90)
t.penup()
t.forward(8*k)
t.right(90)
t.back(3*k)
t.left(90)
t.pendown()
for _ in range(2):
    t.forward(16*k)
    t.right(90)
    t.forward(8*k)
    t.right(90)


t.done() # 249

import turtle as t

k = 20
t.tracer(5)

t.penup()
for x in range(-30*k, 30*k, k):
    for y in range(-40*k, 40*k, k):
        t.goto(x,y)
        t.dot(5, 'purple')
t.goto(0,0)
t.pendown()
for _ in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(18*k)
    t.right(90)
t.penup()
t.forward(5*k)
t.right(90)
t.forward(7*k)
t.left(90)
t.pendown()
for _ in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(7*k)
    t.right(90)

t.done() #



import turtle as t

k = 20
t.tracer(5)

t.penup()
for x in range(-30*k, 40*k, k):
    for y in range(-60*k, 40*k, k):
        t.goto(x,y)
        t.dot(5, 'purple')
t.goto(0,0)
t.pendown()

for l in range(2):
    t.forward(13*k)
    t.right(90)
    t.forward(18*k)
    t.right(90)
t.penup()
t.forward(5*k)
t.right(90)
t.forward(9*k)
t.left(90)
t.pendown()
for i in range(2):
    t.forward(11*k)
    t.right(90)
    t.forward(7*k)
    t.right(90)


t.done()


import turtle as t

k = 20
t.tracer(5)

t.penup()
for x in range(-30*k, 40*k, k):
    for y in range(-60*k, 40*k, k):
        t.goto(x,y)
        t.dot(5, 'purple')
t.goto(0,0)
t.pendown()

for l in range(2):
    t.forward(13*k)
    t.right(90)
    t.forward(18*k)
    t.right(90)
t.penup()
t.forward(5*k)
t.right(90)
t.forward(9*k)
t.left(90)
t.pendown()
for i in range(2):
    t.forward(11*k)
    t.right(90)
    t.forward(7*k)
    t.right(90)


t.done()



