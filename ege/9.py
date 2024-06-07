f = open('../file.txt').read().split('\n')
c = 0


#6 - ans: 412

for line in f:
    row = list(map(int, line.split('\t')))

    cr2 = 0
    cr3 = 0

    for el in row:
        if el % 3 == 0:
            cr3 +=1
        if el % 2 == 0:
            cr2 += 1
    if cr3 <= cr2:
        c +=1

print(c)




# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# — наибольшее из четырёх чисел меньше суммы трёх других;
# — в строке встречается простое число
#
# В ответе запишите только число.
f = open('../file.txt').read().split('\n')
c = 0


def prime(x):
    for d in range(2, int(x**0.5 + 1)):
        if x%d == 0:
            return False
    return  True
print(prime(23))


c = 0
for row in f:
    line = list(map(int, row.split('\t')))
    line.sort()

    c_prime = 0

    if line[3] < (sum(line)-line[3]) :
        for el in line:
            if prime(el) == True:
                c_prime += 1
                break
    if c_prime == 1 :
        c += 1

print(c)


# Определите количество строк таблицы, содержащих числа,
# для которых выполнены оба условия:
# — каждое число в строке встречается по одному разу,
# — утроенная сумма максимального и минимального значений
# не превышает удвоенной суммы оставшихся чисел.


f = open('../file.txt').read().split('\n')
c = 0
for row in f:
    row_int = list(map(int, row.split('\t')))
    row_int.sort()
    s_max_min = (row_int[0]+row_int[4])*3
    s_ost = (row_int[1] + row_int[2] + row_int[3])*2
    if (len(set(row_int)) == len(row_int)) and (s_ost >= s_max_min):
        c += 1

print(c)
 #853






# Откройте файл электронной таблицы, содержащей в каждой строке четыре
# натуральных числа. Определите количество строк таблицы, содержащих числа,
# для которых выполнены оба условия:
# — наибольшее из четырёх чисел меньше суммы трёх других;
# — среди четырёх чисел совпадают ровно два
# (например, четверка чисел 12,12,13,29  подходит,
# а четверка чисел 12,12,12,29   — нет).
# В ответе запишите только число.

f = open('../file.txt').read().split('\n')
c = 0
for row in f:
    row_int = list(map(int, row.split('\t')))
    row_int.sort()
    s = row_int[0] + row_int[1] + row_int[2] # 1 условие

    sovp = 0
    for el in row_int:
        if row_int.count(el) == 2 :
            sovp += 1

    if (row_int[3] < s) and (sovp == 2):
        c += 1

print(c)
 #24


# 6
f = open('text.txt').read().split('\n')
c = 0
for row in f:
    row_int = list(map(int, row.split('\t')))
    row_int.sort()
    k = 0
    sovp = 0

    for el in row_int:
        if row_int.count(el) == 3:
            sovp += 1
            k = el
            for item in row_int:
                if item == 2:
                    row_int.remove(item)
if sovp == 1 and k >= sum(row_int) / 4:
    c += 1
print(c)

# В файле электронной таблицы в каждой строке содержатся четыре натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – наибольшее из четырёх чисел меньше суммы трёх других;
# – среди четырех чисел есть только одна пара равных чисел.

# f = open('text.txt').read().split('\n')
# c = 0
# for row in f:
#     row_int = list(map(int, row.split('\t')))
#     row_int.sort()
#
#     sovp = 0
#     for el in row_int:
#         if row_int.count(el) == 2 :
#             sovp += 1
#
#     if sovp == 1 and (row_int[3] <= (row_int[0] + row_int[1] + row_int[2])):
#         c += 1
# print(c)

f = open('text.txt').read().split('\n')
c = 0
for row in f:
    row_int = list(map(int, row.split('\t')))
    row_int.sort()
    s = row_int[0] + row_int[1] + row_int[2] # 1 условие

    sovp = 0
    for el in row_int:
        if row_int.count(el) == 2 :
            sovp += 1

    if (row_int[3] < s) and (sovp == 2):
        c += 1
print(c)


# – наибольшее из четырёх чисел меньше суммы трёх других;
# – четыре числа можно разбить на две пары чисел с равными суммами.


f = open('text.txt').read().split('\n')
c = 0
for row in f:
    row_int = list(map(int, row.split('\t')))
    row_int.sort()
    s = row_int[0] + row_int[1] + row_int[2] # 1 условие

    sovp = 0
    for el in row_int:
        if row_int.count(el) == 2 :
            sovp += 1


    if (row_int[3] < s) and (row_int[0] + row_int[3] == row_int[1]+row_int[2]):
        c += 1
print(c)


# — в строке только одно число повторяется ровно два раза, остальные числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.

f = open('text.txt').read().split('\n')
c = 0
k = 0
for row in f:
    row_int = list(map(int, row.split('\t')))
    row_int.sort()

    k_2 = 0
    k_1 = 0
    sum_pvtr = 0
    sum_nepvt = 0
    for el in row_int:
        if row_int.count(el) == 2 :
            k_2 += 1
            sum_pvtr = el
        if row_int.count(el) == 1 :
            k_1 += 1
            sum_nepvt += el




    if (k_2 == 2) and (k_1 == 4) and (sum_pvtr*2 <= (sum_nepvt/4)):
        c += 1
print(c)

#445


# 1) Одно число встречается 2 раза, остальные различны
# 2) Хотя бы одно из чисел строки кратна минимальной из сумм строк файла отличной от 0
f = open('text.txt').read().split('\n')
c = 0
lst = []
mn = 10**5
k = 0
for row in f:
    row_int = list(map(int, row.split('\t')))
    if sum(row_int) < mn:
        mn = sum(row_int)

for row in f:
    row_int = list(map(int, row.split('\t')))
    k_2 = 0
    k_1 = 0
    sum_pvtr = 0
    sum_nepvt = 0
    for el in row_int:
        if row_int.count(el) == 2 :
            k_2 += 1
            sum_pvtr = el
        if row_int.count(el) == 1 :
            k_1 += 1
            sum_nepvt += el
        if el % mn == 0:
            k += 1

    if (k_2 == 2) and (k_1 == 3) and (k>0):
        c += 1
print(c)
#564

"""
В каждой строке электронной таблицы записаны шесть натуральных чисел. Определите количе‐
ство строк таблицы, содержащих числа, для которых одновременно выполнены все следующие усло‐
вия:
— все числа в строке различны;
— среднее арифметическое наибольшего и наименьшего чисел в строке больше среднего арифме‐
тического всех остальных чисел.
В ответе запишите число — количество строк, удовлетворяющих заданным условиям.

"""

f = open('text.txt').read().split('\n')
c = 0
for row in f:
    r = list(map(int, row.split('\t')))
    r.sort()
    print(r)
    if r[0] != r[1] != r[2] != r[3] != r[4] != r[5]:
        if (r[0]+r[5])/2 > (r[1]+r[2]+r[3]+r[4])/4:
            c+=1
print(c)

    #
    # for el in row_int:
    #     pass

