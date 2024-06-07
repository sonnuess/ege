"""
Текстовый файл состоит не более чем из 10^6   символов A, B, C. Определите длину самой длинной последовательности идущих подряд символов B  .
Для выполнения этого задания следует написать программу. В ответе запишите длину искомой последовательности.
"""

s = open('file.txt').read()
l = 0
ans = 0
for i in range(len(s) - 1):
    a, b = s[i], s[i+1]

    if a == 'B' and b == 'B':
        l += 1

    if a == 'B' and b != 'B':
        ans = max(l, ans)
        l = 0

    if a != 'B' and b == 'B':
        l = 1

if l > ans:
    ans = l

print(ans)
# 12

"""
Текстовый файл состоит не более чем из 10**6   символов A  , B  , C  , D  , E  . Найдите модуль разности между длинами максимальной подпоследовательности,
состоящей только из символов A  , и максимальной подпоследовательности, состоящей только из символов B  .
Для выполнения этого задания следует написать программу. Воспользуйтесь файлом "Задание_7_ДЗ". В ответе запишите искомую разность.
"""

s = open('file.txt').read()
lA = 0
lB = 0
ansA =0
ansB = 0
for i in range(len(s) - 1):
    a, b = s[i], s[i+1]

    if a == 'A' and b == 'A':
        lA += 1
    if a == 'B' and b == 'B':
        lB += 1

    if a == 'A' and b != 'A':
        ansA = max(lA, ansA)
        lA = 0
    if a == 'B' and b != 'B':
        ansB = max(lB, ansB)
        lB = 0

    if a != 'A' and b == 'A':
        lA = 1
    if a != 'B' and b == 'B':
        lB = 1

print(ansA) # 8
print(ansB) # 8
print(ansA - ansB) # 0

"""
Текстовый файл состоит не более чем из 10^6   символов A  , B  , C  . Определите длину максимальной последовательности подряд идущих символов, где все символы одинаковые.
Для выполнения этого задания следует написать программу. Воспользуйтесь файлом "tcex". В ответе запишите длину искомой последовательности.
"""

s = open('file.txt').read()
l = 1
ans = 0
for i in range(len(s) - 1):
    a, b = s[i], s[i+1]

    if a == b:
        l += 1

    if a != b:
        ans = max(l, ans)
        l = 1


ans = max(l, ans)
print(ans)
# 14

"""
Текстовый файл состоит не более чем из 10**6 заглавных букв латинского алфавита. Найдите последовательность максимальной длины,
которая содержит буквы строго в алфавитном порядке, т.е. ABCD...  .
Для выполнения этого задания следует написать программу.
"""
st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = open('file.txt').read()
l = 0
ans = 0

for i in range(len(s) - 1):
    a, b = s[i], s[i+1]

    if a < b:
        l += 1

    if a >= b:
        ans = max(l, ans)
        l = 0




print(ans)
# ? (7)



"""
Текстовый файл состоит не более чем из 10^6   символов P,K.
Найдите из запишите в ответ количество подстрок PK   в файле. Для последовательности PKKPPK   ответом будет 2.
Для выполнения этого задания следует написать программу.
"""
s = open('file.txt').read()
ans = 0

for i in range(len(s) - 1):
    a, b = s[i], s[i+1]
    if a == 'P' and b == 'K':
        ans += 1


print(ans)

s = s.replace('PK', 'x')
print(s.count('x'))
# 249736

"""
Текстовый файл состоит из символов S, R, O. Определите максимальную длину подстроки, состоящей из троек символов OSR или RSO.
Искомая подстрока может включать только тройки OSR, только тройки RSO или содержать одновременно как тройки OSR, так и тройки RSO. Тройки не могут пересекаться.
"""
s = open('file.txt').read()
ans = 0
c = 0
for i in range(0, len(s) - 2):
    a, b, c = s[i], s[i + 1], s[i + 2]
    if a + b + c == 'OSR' or a + b + c == 'RSO':
        k = 0
        for l in range(i, len(s) - 2, 3):
            a, b, c = s[l], s[l+1], s[l+2]
            if a + b + c == 'OSR' or a + b + c == 'RSO':
                k += 1
            else:
                break
            ans = max(ans, k)

print(ans) # 5 по 3
# 15


"""
Текстовый файл состоит из символов S, R, O. Определите максимальную длину подстроки, состоящей из троек символов OSR или RSO.
Искомая подстрока может включать только тройки OSR, только тройки RSO или содержать одновременно как тройки OSR, так и тройки RSO. Тройки не могут пересекаться.
"""
s = open('file.txt').read()
ans = 0
c = 0
for i in range(0, len(s) - 2):
    a, b, c = s[i], s[i + 1], s[i + 2]
    if a + b + c == 'OSR' or a + b + c == 'RSO':
        k = 0
        for l in range(i, len(s) - 2, 3):
            a, b, c = s[l], s[l + 1], s[l + 2]
            if a + b + c == 'OSR' or a + b + c == 'RSO':
                k += 1
            else:
                break
            ans = max(ans, k)

print(ans)  # 5 по 3
# 15

# or
f = open('24__tlln.txt').read()

i = 0
ans = 0
k = 0
while i < len(f) - 2:
    a, b, c = f[i], f[i + 1], f[i + 2]

    if a + b + c == 'RSO' or a + b + c == 'ORS':
        # либо тройка подошла
        k += 3
        i += 3
    else:
        # либо не подошла
        ans = max(ans, k)
        k = 0
        i += 1

print(ans)


f = open('file.txt').read()
s = 'QSR'
ans = 0
k = 1
for i in range(0, len(f) - 1):
    a, b = f[i], f[i+1]
    # не подходит
    if ((a in s) and (b not in s)) or ((a not in s) and (b in s)) or ((a not in s) and (b not in s)):
        k += 1
    else:
        ans = max(ans, k)
        k = 1
print(ans, k)
# 544

f = open('file.txt').read()

ans = 0
k = 1
for i in range(0, len(f) - 1):
    a, b = f[i], f[i + 1]
    if a != b:
        k += 1
    else:
        ans = max(k, ans)
        k = 1

ans = max(ans, k)
print(ans)

# abcaabcbbcabcbacb


"""
№2 Текстовый файл состоит не более чем из 10^6   символов А, М и R. Определите общее количество сочетаний символов типа AR или AM. Для выполнения этого задания следует написать программу. 
Гарантируется, что хотя бы одно из таких сочетаний есть.
Например, в последовательности символов AARMAM, идущих подряд, есть две подходящие пары символов."""
f = open('file.txt').read()
f = f.replace('AM', 'x')
f = f.replace('AR', 'x')
print(f.count('x'))
#2123


"""
№3 Текстовый файл состоит не более чем из 10^6   цифр от 0 до 9. Найдите самую длинную последовательность, цифр одной четности.
Для выполнения этого задания следует написать программу. В ответе запишите длину искомой последовательности.
"""
f = open('file.txt').read()
ch = '02468'
ne = '13579'
k = 1
ans = 0
for i in range(len(f) - 1):
    a, b = f[i], f[i+1]
    if ((a in ch) and (b in ch)) or ((a in ne) and (b in ne)):
        k += 1
    else:
        ans = max(ans, k)
        k = 1
print(ans, k)
# 11

"""
№4 Текстовый файл состоит не более чем из 10^6   заглавных букв латинского алфавита.
Найдите самый часто повторяющийся символ между символами A   и R   (в данном порядке: A   *символ* R  ). Если таких символов несколько, следует взять тот, что раньше по алфавиту.
Для выполнения этого задания следует написать программу.
"""
f = open('file.txt').read()
ans = 0
lib = {}
for i in range(len(f)):
    if f[i] == 'A':
        a = i

    if f[i] == 'R':
        r = i


for i in range(a + 1, r):
    n = f[i]
    if n not in lib.keys():
        lib[n] = 1
    if n in lib.keys():
        lib[n] += 1

print(max(lib.values()))
print(lib)
# B

"""
№5 Текстовый файл состоит не более чем из 10^6   заглавных букв латинского алфавита.
Найдите последовательность максимальной длины, где символы идут в порядке «больше», «меньше», «больше», «меньше» и т.д. по таблице ASCII. Пример подходящей последовательности: BABACADB  .
Для выполнения этого задания следует написать программу.
"""
f = open('file.txt').read()
ans = 0
k = 0
flag = True
for i in range(len(f) - 1):
    a, b = f[i], f[i+1]
    if a > b and flag:
        k += 1
        flag = False
    elif a < b and not flag:
        k += 1
        flag = True # Ждем больше
    elif a > b and not flag:
        k = 2
    elif a < b and flag:
        k = 1
    else:
        k = 1
    ans = max(k, ans)
print(ans)
# 19

"""
Текстовый файл содержит строку из символов A, B, C и цифр 1, 2, 3, всего не более чем 10^6 символов.
Определите максимальное количество идущих подряд троек символов вида «буква + цифра + буква».
"""
f = open('text.txt').read()

i = 0
ans = 0
k = 0
l = 'ABC'
m = '123'
while i < len(f) - 2:
    a, b, c = f[i], f[i+1], f[i+2]
    if (a in l) and (b in m) and (c in l):
        k += 1
        i += 3
    else:
        ans = max(k, ans)
        k = 0
        i += 1

print(ans, k)
# 3 тройки 9 символов


"""
Текстовый файл состоит не более чем из 10^6   символов ’(’ и ’)’.
Вам необходимо узнать какую максимальную длину имеет правильная скобочная последовательность.
Правильная скобочная последовательность - последовательность скобок, которая подчиняется нескольким правилам:
1) Последовательность начинается с открывающейся скобки
2) Каждая открывающаяся скобка имеет в пару закрывающаяся скобку
3) Количество открывающихся скобок в любой точке скобочной последовательности больше либо равно количеству закрывающихся
Примеры правильных скобочных последовательностей: ()()()  , ()(()())
"""
f = open('file.txt').read()
left = 0
right = 0
ans = 0
for i in range(1, len(f)):
    if f[i] == '(':
        left += 1
    if f[i] == ')':
        right += 1
        if left > right:
            ans = max(ans, 2 * right)

        if left == right:
            ans = max(ans, left + right)

        if right > left:
            right = 0
            left = 0

print(ans)
# 6822

"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
Текст разбит на строки различной длины. Необходимо найти строку, содержащую наибольшее количество пар соседних букв,
которые стоят в таком же порядке как и в алфавите (например, AB, BC, CD и т.д.; в цепочке ABC две таких пары). Если таких строк несколько, надо взять ту, которая в файле встретилась раньше.
Выведите максимальное количество пар, встреченных среди всех строк, а также букву из данной строки, которая встречается чаще всего, если таких букв несколько, то выведите ту, что раньше стоит по алфавиту.
Пример. Исходный файл:
ZCQABA
ZALMAC
CRACUT
В этом примере в первой и второй строках по одной подходящей паре (AB и LM), в третьей таких пар нет.
Берём первую строку, т.к. она раньше встречается в файле. В этой строке чаще других встречается буква А. Если бы она была не единственной, то выбрали ту букву, что раньше стоит в алфавите.
В ответе для этого примера надо записать 1A.
"""
f = open('file.txt').read().split('\n')
k = 0
st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0
lib = {}
for s in f:
    k = 0
    for i in range(len(s) - 1):
        a, b = s[i], s[i+1]
        if a+b in st:
            k += 1
        else:
            ans = max(k, ans)
            if ans not in lib.keys():
                lib[ans] = [s]
            else:
                lib[ans].append(s)
print(ans, k)
l = lib[ans][0]
dict = {}
for el in  l:
    if el not in dict.keys():
        dict[el] = 1
    else:
        dict[el] += 1
print(dict)
#31C


"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z). Текст разбит на строки различной длины.
Необходимо найти строку, содержащую наибольшее количество пар соседних букв, которые стоят в таком же порядке как и в алфавите (например, AB, BC, CD и т.д.; в цепочке ABC две таких пары).
Если таких строк несколько, надо взять ту, которая первая в алф порядке.
Выведите максимальное количество пар, встреченных среди всех строк, а также букву из данной строки, которая встречается чаще всего.
Пример. Исходный файл:
ZCQABA
ZALMAC
CRACUT
В этом примере в первой и второй строках по одной подходящей паре (AB и LM), в третьей таких пар нет.
Берём первую строку, т.к. она раньше встречается в файле. В этой строке чаще других встречается буква А.
Если бы она была не единственной, то выбрали ту букву, что раньше стоит в алфавите. В ответе для этого примера надо записать 1A.
"""

f = open('file.txt').read().split('\n')
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lib = {}
for row in f:
    k = 0  # count of pairs
    for i in range(len(row) - 1):
        a, b = row[i], row[i+1]
        if s.index(a) == s.index(b) - 1:
            k += 1

    if k not in lib.keys():
        lib[k] = [row]
    else:
        lib[k].append(row)

m = max(lib.keys())
lib[m].sort()
r = lib[m][0]
dict = {}
for el in r:
    if el not in dict.keys():
        dict[el] = 1
    else:
        dict[el] += 1

print(dict)
print(max(dict.values()))
# 50Y

"""
Текстовый файл состоит не более чем из 10^4   строк, каждая из которых состоит не более чем из 10^4   заглавных букв латинского алфавита.
В строке, содержащей не менее 150 символов Z   найдите максимальное расстояние (разница в индексах) между двумя одинаковыми символами, между которым не повторяется этот символ.
Если строк, содержащих не менее 150 символов Z  несколько, то используйте последнюю из таковых для поиска маскимального расстояния.
Пример:
ABBAC
PRE  r EOOOOO r
QWERTYQ
Среди данных строк нет ни одной, где количесто символов Z   не менее 150.
Если забыть про это условие (в рамках примера), то максимальное расстояние между символами R   во второй строке и оно равно 7.
"""

f = open('file.txt').read().split('\n')
lib = {}
l = []
for p in f:
    k = 0  # count of pairs
    if p.count('Z') >= 150:
        l.append(p)
print(l)
row = l[-1]
for i in range(len(row) - 1):
    a, b = row[i], row[i+1] # z a / z z / v z / a b
    if a == 'Z' and b != 'Z':
        k += 1
    if a != 'Z' and b != 'Z' and k > 0:
        k += 1
    if a != 'Z' and b == 'Z':
        if k not in lib.keys():
            lib[k] = [row]
        k = 0
    if a == 'Z' and b == 'Z':
        k = 0

m = max(lib.keys())
r = lib[m][-1]
print(m)
# 196

"""
Для каждой строки нужно определить букву (или буквы), которая встречается в этой строке чаще всего после буквы X.
Все эти буквы добавляются в новый список. Найдите букву, которая чаще всего встречается в построенном списке, и в качестве ответа укажите, сколько раз она там встретилась.
Например, пусть файл содержит две строки:
XAXBXAXBCXX
BXAXCXCXAXD
В первой строке чаще всего после буквы X встречаются буквы А и B (по 2 раза), а во второй строке – буквы A и С (по 2 раза).
В итоге должен быть построен список [A, B, A, C], в котором чаще всего (2 раза) встречается буква A. Ответ: 2.
"""

f = open('file.txt').read().split('\n')
lib = {}
l = []
for row in f:
    for i in range(len(row) - 1):
        a, b = row[i], row[i+1]
        if a == 'X' and b != 'X':
            if b not in lib.keys():
                lib[b] = 1
            else:
                lib[b] += 1

            m = max(lib.values())
            for k, v in lib.items():
                if v == m:
                    l.append(k)
dict = {}
for el in l:
    if el not in dict.keys():
        dict[el] = 1
    else:
        dict[el] += 1

print(dict)
print(max(dict.values()))


f = open('file.txt').read()
k = 0
l = 'RSQ'
ans = 0

for i in range(len(f) - 2):
    a, b, c = f[i], f[i+1], f[i+2]
    if a+b+c == 'RSQ':
        if f[i-1]+f[i-2] == 'SQ':
            k += 2
        elif f[i-1] == 'Q':
            k += 1
        for l in range(i, len(f) - 2, 3):
            a, b, c = f[l], f[l+1], f[l+2]
            if a+b+c == 'RSQ':
                k += 3
            else:
                if f[i+3] == 'S':
                    k += 1
                elif f[i+3] + f[i+4] == 'SR':
                    k += 2
                break
            ans = max(ans, k)
            k = 0
print(ans)


f = open('file.txt').read()

k = 0
ans = 0

for i in range(len(f) - 5):
    a, b, c, d, e = f[i], f[i+1], f[i+2], f[i+3], f[i+4]
    if a+b+c+d+e == 'VWXYZ':
        k = 0
        for l in range(i, len(f) - 5, 5):
            a, b, c, d, e = f[l], f[l+1], f[l+2], f[i+3], f[i+4]
            if a+b+c+d+e == 'VWXYZ':
                k += 1
            else:
                break
            ans = max(ans, k)
print(ans*5)

f = open('file.txt').read()
# c = 0
# ans = 0
# for i in range(len(f) - 1):
#     a, b = f[i], f[i+1]
#     if a != b:
#         c += 1
#     else:
#         ans = max(ans, c)
#         c = 1
# print(ans, c)


# st = 'GWP'
# ans = 0
# c = 0
# for el in f:
#     if el not in st:
#         c += 1
#
#     else:
#         ans = max(ans, c)
#         c = 0
# print(ans, c)


# ans = 0
# c = 0
# i = 0
# while i < len(f) - 1:
#     a, b = f[i], f[i+1]
#     if ((a + b) == 'AB') or ((a + b) == 'AC'):
#         c += 1
#         i += 2
#     else:
#         ans = max(ans, c)
#         c = 0
#         i += 1
# print(ans, c)


# g = 'AO'
# s = 'BCD'
# i = 0
# c = 0
# ans = 0
# while i < len(f) - 1:
#     a, b = f[i], f[i+1]
#     if a in s and b in g:
#         c += 1
#         i += 2
#     else:
#         ans = max(ans, c)
#         c = 0
#         i += 1
# print(ans, c)



# ans = 0
# k = 0
# i = 0
# while i < len(f) - 2:
#     a, b, c = f[i], f[i+1], f[i+2]
#     if a+b+c == 'NPO' or a+b+c == 'PNO':
#         k += 1
#         i += 3
#     else:
#         ans = max(ans, k)
#         k = 0
#         i += 1
# print(ans, k)


# ans = 0
# c = 0
# st = 'XYZ'
# for i in range(len(f) - 1):
#     a, b = f[i], f[i+1]
#     if ((a not in st) and (b not in st)) or ((a not in st) and (b in st)) or ((a in st) and (b not in st)):
#         c += 1
#     else:
#         ans = max(c, ans)
#         c = 1
# print(ans, c)


# f = f.split('Y')
# ans = 0
# for i in range(len(f)-151):
#     c = 'Y'.join(f[i:i+151])
#     c = len(c)
#     ans = max(c, ans)
# print(ans)


# i = 0
# ans = 0
# s = 'ABCDEF'
# l = '0123456789'
# c = 0
# while i < len(f):
#     a = f[i]
#     if ((a in s) or (a in l)):
#         c += 1
#         i += 1
#     else:
#         ans = max(c, ans)
#         c = 0
#         i += 1
# print(ans, c)

# s = 'ABC'
# l = '89'
# ans = 0
# c = 1
# flag = False
# for i in range(len(f)):
#     el = f[i]
#     if el in s and flag == False:
#         c += 1
#         flag = True
#         ans = max(ans, c)
#     elif el in l and flag == False:
#         ans = max(ans, c)
#         c = 1
#     elif el in s and flag == True:
#         ans = max(ans, c)
#         c = 1
#     elif el in l and flag == True:
#         c += 1
#         flag = False
#         ans = max(ans, c)
# print(ans, c)

# ans = 0
# k = 0
# l = 0
# for r in range(len(f)):
#     if f[r] == 'T':  k += 1
#     while k > 100:
#         if f[l] == 'T': k -= 1
#         l += 1
#     if k == 100:
#         ans = max(ans, r-l+1)
# print(ans)


s = 'ABC'
l = '6789'
c = 0
ans = 0
flag = True
for el in f:
    if el in s and flag == True:
        ans = max(ans, c)
        c = 1
    elif el in s and flag == False:
        c += 1
        flag = True
    elif el in l and flag == False:
        ans = max(ans, c)
        c = 1
    elif el in l and flag == True:
        c += 1
        flag = False


print(ans)


f = open('file.txt').read()
flag = False
st = 'DSMREAIK'
ans = 0
c = 0
for i in range(len(f)):
    el = f[i]
    if el in st:
        c += 1
    else:
        ans = max(c, ans)
        c = 0
print(ans, c)


f = open('file.txt').read()
ans = 0
counter = 0
i = 0
while i < len(f) - 2:
    a, b, c = f[i], f[i+1], f[i+2]
    if a+b+c == 'RSO' or a+b+c == 'OSR':
        counter += 1*3
        i += 3
    else:
        ans = max(ans, counter)
        counter = 0
        i += 1
print(ans, counter)


f = open('file.txt').read()
ans = 0
counter = 1
for i in range(len(f) - 1):
    if f[i] != f[i+1]:
        counter += 1
    else:
        ans = max(ans, counter)
        counter = 1
print(ans)


f = open('file.txt').read()
ans = 0
counter = 1
for i in range(len(f) - 1):
    if int(f[i])%2 == int(f[i+1])%2:
        counter += 1
        ans = max(ans, counter)
    else:
        counter = 1
print(ans, counter)

f = open('file.txt').read()
ans = 0
counter = 1
for i in range(len(f) - 1):
    if ord(f[i]) == (ord(f[i+1]) - 1):
        counter += 1
        ans = max(ans, counter)
    else:
        counter = 1
print(ans, counter)


f = open('file.txt').read()
ans = 0
s = 'BCD'
g = 'AO'
flag = False
counter = 1
for i in range(len(f)):
    el = f[i]
    if ((el in s) and (flag == False)) or ((el in g) and (flag == True)):
        ans = max(ans, counter)
        counter = 1/2
    elif (el in g) and (flag == False):
        flag = True
        counter += 1/2
    elif (el in s) and (flag == True):
        flag = False
        counter += 1/2

print(ans, counter)


f = open('file.txt').read()
counter = 0
ans = 0
i = 0
while i < len(f) - 2:
    a, b, c = f[i], f[i+1], f[i+2]
    if a+b+c == 'NPO' or a+b+c == 'PNO':
        counter += 1
        i += 3
    else:
        ans = max(ans, counter)
        counter = 0
        i += 1
print(ans, counter)

f = open('file.txt').read()
ans = 0
s = 'CDF'
g = 'AO'
flag = False
counter = 0
for i in range(len(f)):
    el = f[i]
    if ((el in s) and (flag == False)) or ((el in g) and (flag == True)):
        ans = max(ans, counter)
        counter = 0
    elif (el in g) and (flag == False):
        flag = True
        counter += 1
    elif (el in s) and (flag == True):
        flag = False
        counter += 1

print(ans, counter)


f = open('file.txt').read()
ans = 0
s = 'XYZ'
flag = False
counter = 1
for i in range(len(f)-1):
    a, b = f[i], f[i+1]
    if ((a not in s) and (b not in s)) or ((a in s) and (b not in s)) or ((a not in s) and (b in s)):
        counter += 1
    else:
        ans = max(counter, ans)
        counter = 1
print(ans, counter)

f = open('file.txt').read()
ans = 0
f = f.split('Y')
for i in range(len(f)-151):
    curr = 'Y'.join(f[i:i+151])
    ans = max(ans, len(curr))
print(ans)

f = open('file.txt').read()
ans = 0
counter = 0
st = '0123456789ABCDEF'
for i in range(len(f)):
    el = f[i]
    if el in st:
        counter += 1
    else:
        ans = max(ans, counter)
        counter = 0
print(ans)



f = open('file.txt').readline()
l = m = k = 0
for r in range(len(f)):
    if f[r] == 'T':
        k += 1
    while k > 100:
        if f[l] == 'T':
            k -= 1
        l += 1
    m = max(r - l + 1, m)
print(m)

f = open('file.txt', 'r')
s = f.readline()
count_t, end, ma = 0,0,0
for start in range(len(s)-1):
    if s[start] == 'T':
        count_t += 1
    while count_t > 100:
        if s[end] == 'T':
            count_t -= 1
        end += 1
    ma = max(ma,start-end+1)
print(ma)


f = open('file.txt').read()
ans = 0
s = 'QRW'
g = '124'
flag = False
counter = 1
for i in range(len(f)):
    el = f[i]
    if ((el in s) and (flag == False)) or ((el in g) and (flag == True)):
        ans = max(ans, counter)
        counter = 1
    elif (el in g) and (flag == False):
        flag = True
        counter += 1
    elif (el in s) and (flag == True):
        flag = False
        counter += 1

print(ans, counter)
