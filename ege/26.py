# v = 20 k = 2
f = open('file.txt').read().split()
f = list(map(int, f))
f = sorted(f)
f = f[::-1]
k1 = 0
k2 = 0
counter = 0
for i in f:
    if k1 + i <= 4444:
        k1 += i
        counter += 1
    else:
        if k2 + i <= 4444:
            k2 += i
            counter += 1
print(sum(f) - k1 - k2)
print(len(f) - counter)


f = open('file.txt').read().split()
f = list(map(int, f))
f = sorted(f)
print(f)
s = 0
l = []
users = 0
# s = 53478
# users = 6638
for a in range(len(f)):
    i = f[a]
    if s+i <= 53478:
        l.append(i)
        s += i
        users += 1
    else:
        break
print(s)
print(i)
print(s-i)
print(53478-s+i)
print(users)









f = open('file.txt').read().split()
f = list(map(int, f))
f = sorted(f)
print(f)
s = 0
l = []
users = 0
# 75483 9830
for a in range(len(f)):
    i = f[a]
    if s+i <= 75483:
        l.append(i)
        s += i
        users += 1
    else:
        break
print(75483 - s)
print(i)
print(75483-s+26)
print(s-1)
# 27 103
# 26 10

films = [[3, 5], [4, 9], [5, 8]]
films.sort()
print(films)
f = [3, 5, 4, 9, 5, 8]
ans = 0
c = 0
flag = 0
for t in range(min(f), max(f) + 1):
    for film in films:
        if t == film[1] and flag == film: # 1 ?????
            flag = 0

    for film in films:
        if t == film[0]:
            if flag == 0:
                flag = film
                c += 1
            else:
                if flag[1] > film[1]:
                    flag = film


print(c)


f = [17, 15, 14, 12, 11, 8, 6, 5, 4, 2]
n = 30
ans = 0
curr = []
last_successful_el = 0
while sum(f) > n:
    curr.append(f[0])
    del f[0]

    if sum(curr) == n:
        ans += len(curr) - 1

        curr = []
        last_successful_el = 0
        f.sort(reverse=True)
    elif sum(curr) > n:
        last_successful_el = curr[-1]
        del curr[-1]
        f.append(last_successful_el)
    elif sum(curr) < n:
        if last_successful_el != 0:
            f.append(curr[-1])
            f.remove(last_successful_el)
            del curr[-1]

            curr.append(last_successful_el)
            ans += (len(curr)-1)
            f.append(sum(curr)-n)

            curr = []
            last_successful_el = 0
            f.sort(reverse=True)


print(ans, f)

guests = [[5, 8], [2, 4], [3, 9]]
guests.sort()
c = 0
ans = 0

for t in range(2, 9+1):
    c = 0
    for guest in guests:
        if t >= guest[0] and t <= guest[1]:
            c += 1
    ans = max(c, ans)

print(ans)


guests = [[5, 8], [2, 4], [3, 9]]
guests.sort()
c = 0
ans = 0

for t in range(2, 9+1):
    for guest in guests:
        if guest[0] == t:
            c += 1
        if guest[1] == t:
            c -= 1

    ans = max(c, ans)

print(ans)

'''
Система наблюдения ежеминутно фиксирует вход и выход посетителей магазина (в минутах, прошедших от начала суток).
Считается, что в моменты фиксации входа и выхода посетитель находится в магазине. Нулевая минута соответствует моменту открытия магазина, который работает 24 ч в сутки без перерыва.
Менеджер магазина анализирует данные системы наблюдения за прошедшие сутки, и выявляет отрезки времени наибольшей длины, в течение которых число посетителей,
находящихся в магазине, не изменялось.
Далее менеджер выбирает пики посещаемости — промежутки времени, когда количество посетителей в магазине было наибольшим. Пиков посещаемости в течение суток может быть несколько.
Входной файл содержит время входа и выхода каждого посетителя магазина. Определите, сколько пиков посещаемости было в течение суток, и укажите число посетителей в момент пика посещаемости.
Входные данные
В первой строке входного файла находится натуральное число N (N < 10000) - количество посетителей магазина.
Следующие N строк содержат пары чисел, обозначающих соответственно время входа и время выхода посетителя (все числа натуральные, не превышающие 1440).
Запишите в ответе два натуральных числа: сначала найденное количество пиков посещаемости, а затем число посетителей в момент пика посещаемости.
Типовой пример организации данных во входном файле
6
10 50
100 150
110 155
120 160
130 170
151 170
При таких исходных данных было два пика посещаемости: в отрезки времени со 130 по 150 минуты и со 151 по 155 минуты. Число посетителей в момент пика посещаемости равно 4.
Типовой пример имеет иллюстративный характер. Для выполнения задания используйте данные из прилагаемых файлов.
'''
f = open('file.txt').read().split('\n')
for i in range(len(f)):
    f[i] = list(map(int, f[i].split()))
f.sort()
peak = 0
counter_of_peaks = 0
x = 0
for t in range(1, 1440):
    c = 0
    for guest in f:
        if (t >= guest[0]) and (t <= guest[1]):
            c += 1
    if c > peak:
        peak = c
        counter_of_peaks = 1
        x = t
    elif c == peak and (t != x+1):
        counter_of_peaks += 1
    elif c == peak and t == x+1:
        x = t
print(counter_of_peaks, peak)



# 210 - 600
f = open('file.txt').read().split('\n')
for i in range(len(f)):
    f[i] = list(map(int, f[i].split()))
f = sorted(f)

busy_box = 0
baggage = 0
boxes = []
for t in range(1440):
    for pas in f:
        if pas[0] == t and busy_box < 210:
            busy_box += 1
            for number in range(1, 211):
                if number not in boxes:
                    boxes.append(number)
                    pas.append(number)
                    baggage += 1
                    print(pas)
                    break
    for pas in f:
        if pas[1] == t and len(pas) == 3:
            busy_box -= 1
            boxes.remove(pas[2])
            pas.remove(pas[2])
print(baggage)



'''
На производстве штучных изделий N деталей должны быть отшлифованы и окрашены. Для каждой детали известно время
её шлифовки и время окрашивания. Детали пронумерованы начиная с единицы. Параллельная обработка деталей не предусмотрена.
На ленте транспортёра имеется N мест для каждой из N деталей.
На ленте транспортёра детали располагают по следующему алгоритму:
— все 2N чисел, обозначающих время окрашивания и шлифовки для N деталей, упорядочивают по возрастанию;
— если минимальное число в этом упорядоченном списке — это время шлифовки конкретной детали, то деталь размещают на ленте транспортёра на первое свободное место от её начала;
— если минимальное число — это время окрашивания, то деталь размещают на первое свободное место от конца ленты транспортёра
— если число обозначает время окрашивания или шлифовки уже рассмотренной детали, то его не принимают во внимание.
Этот алгоритм применяется последовательно для размещения всех N деталей.
Определите номер последней детали, для которой будет определено её место на ленте транспортёра, и количество деталей, которые
будут отшлифованы до неё.
Входные данные
В первой строке входного файла находится натуральное число N (N < 1000)- количество деталей. Следующие N строк содержат
пары чисел, обозначающих соответственно время шлифовки и время окрашивания конкретной детали (все числа натуральные, различные).
Запишите в ответе два натуральных числа: сначала номер последней детали, для которой будет определено её место на ленте транспортёра, затем количество деталей, которые будут отшлифованы до неё.
Типовой пример организации данных во входном файле
5
30 50
100 155
150 170
10 160
120 55
При таких исходных данных порядок расположения деталей на ленте транспортёра следующий: 4, 1, 2, 3, 5. Последней займёт своё место на ленте транспортёра деталь 3. При этом до неё будут отшлифованы три детали.
'''
# шлифовка начало - окрашивание конец
f = open('text.txt').read().split('\n')
for i in range(len(f)):
    f[i] = list(map(int, f[i].split()))
f.sort()
l = 997
lenta = []
for i in range(len(f)):
    el = f[i]
    if el[0] < el[1]:
        for place in range(1, 997):
            if place not in lenta:
                lenta.append(place)
    if el[0] > el[1]:
        for place in range(997, 0, -1):
            if place not in lenta:
                lenta.append(place)





'''Вам известны времена прихода и ухода каждого из n   посетителей ресторана. Какое максимальное количество человек посетило ресторан в какой-либо момент времени?
Входные данные:
Первая строка входных данных содержит единственное число n .
Далее следуют n   строк, описывающие клиентов. Каждая строка содержит два числа a   и b  : времена прихода и ухода каждого клиента (1 ≤ a ≤ b ≤ 109)  .
Гарантируется, что все времена захода и ухода различные.
Выведите одно число — максимальное число клиентов в какой-либо момент времени.
Пример входных данных:
3 
5   8  
2   4  
3   9  
Пояснение к примеру:
Например, в момент времени 7   в ресторане присутствовали первый и третий клиент. Ответ на данный пример — 2  .'''
f = open('file.txt').read().split('\n')
for i in range(len(f)):
    f[i] = list(map(int, f[i].split()))
ans = 0
for t in range(1, 110):
    c = 0
    for guest in f:
        a, b, = guest[0], guest[1]
        if (t >= a) and (t <= b):
            c += 1

    ans = max(ans, c)
print(ans)

f = open('file.txt').read().split('\n')
for i in range(len(f)):
    f[i] = list(map(int, f[i].split()))

minutes = [0] * 44641
for t in range(1, 44641):
    for film in f:
        if (film[0] <= t) and (t < film[1]):
            minutes[t] = 1
print(minutes.count(1))
c = 0
ans = 0
for el in minutes:
    if el == 1:
        c += 1
    if el == 0:
        ans = max(ans, c)
        c = 0
print(ans)


#коржи не эксель

k = list(map(int, open('26_16335 (3).txt').read().split('\n')))
k.sort()
k.reverse()
print(k)

tort = [k[0]]
for i in range(len(k)):
    k_A = tort[-1]
    k_B = k[i]
    if k_A - k_B >= 4:
        tort.append(k_B)

print(len(tort), tort[-1])



f = list(map(int, open('file.txt').read().split('\n')))
f.sort(reverse=True)

tort = [f[0]]
for i in range(len(f)):
    korzh_1 = tort[-1]
    korzh_2 = f[i]
    if korzh_1 - korzh_2 >= 8:
        tort.append(korzh_2)

print(len(tort), tort[-1])


