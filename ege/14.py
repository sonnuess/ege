lst = []
n = 7**103 +6*7**104-3*7**57+98
base = 7
while n>0:
    lst.append(n%base)
    n = n // base
print(lst.count(6))


print('NEXT task ')
lst = []
n = 243
base = 2
while n > 0:
    lst.append(n%base)
    n = n // base
print(lst[::-1])


print('NEXT task ')
lst = []
n = 2**51+2**40+2**35+2**17-2**5
base = 16
while n > 0:
    lst.append(n%base)
    n //= base

print(set(lst))

# bin2 oct8 hex16 int10
#set() оставляет только уникальные значения
print('NEXT task ')
n = 256**2 + 4096**16 - 15
base = 16
lst = []
while n > 0 :
    lst.append(n%base)
    n = n // base
print(lst.count(15))
# одно и то же но другой способ
n = 256**2 + 4096**16 - 15
print((hex(n)[2:]).count('f'))



print('NEXT task ')
ans = 0
for i in range (2, 11):

    lst = []
    n = 559
    base = i
    while n > 0 :
        lst.append(n%base)
        n //= base
    if sum(lst) % 2 != 0:
        ans = ans + i
print(ans)


print('NEXT task ')
for x in range(0, 10):
    a = int(f'4c{x}4', 15)
    b = int(f'{x}62a', 13)
    f = a + b
    if f % 121 == 0 :
        print(x)
        print(f//121)
        break


print('NEXT task ')
st = '0123456789abcdef'
for x in st:
    a = int(f'2{x}84', 19)
    b = int(f'2b3{x}', 16)
    f = a + b
    if f % 88 == 0 :
        print(f // 88)

print('NEXT task ')
for x in range(0, 109):
    a = 1 + 5 * 109 + 7 * 109 ** 2 + x * 109 ** 3
    b = x + 7*215 + 3*215**2 + 2*215**3
    f = a + b
    if f % 567 == 0 :
        print(f//567)



print('NEXT task ')

n = 4**103 + 3*4**444 - 2*4**44 + 67
base = 4
lst = []
while n > 0:
    lst.append(n%base)
    n = n // base
print(lst)
print(lst.count(3))
# s = sum(lst)
# print(s)


print('NEXT task ')
# x321 в 111СС + 17x4 в 211СС
for x in range(0, 111):
    a = 1 + 2*111 + 3*111**2 + x*111**3
    b = 4 + x*211 + 7*211**2+ 1*211**3
    f = a + b
    if f % 111 == 0 :
        print(f//111)


print('NEXT task ')
# x751 в 109СС + 237x в 215СС
for x in range(0, 109):
    a = 1 + 5*109 + 7*109**2 + x*109**3
    b = x + 7*215 + 3*215**2 + 2*215**3
    f = a + b
    if f % 567 == 0:
        print(f//567)


#  Значение выражения 6^203 + 5∙6^405 – 3∙6^144 + 76 записали в системе счисления с основанием 6.
# Найдите сумму цифр получившегося числа и запишите её в ответе в десятичной системе счисления.
print('NEXT task ')
n = 6**203 + 5*6**405 - 3*6**144 + 76
base = 6
lst = []
while n > 0 :
    lst.append(n%base)
    n //= base
print(lst)
print(sum(lst))

# Дано арифметическое выражение:
#    12x45 в 98СС + 1x98 в 123СС
# В записи чисел переменной x обозначена неизвестная цифра из допустимого алфавита для указанных систем счисления.
# Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 123.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 123 и укажите его в ответе в десятичной системе счисления.
print('NEXT task ')
for x in range(0, 98):
    a = 5 + 4*98 + x*98**2 + 2*98**3 + 1*98**4
    b = 8 + 9*123 + x*123**2 + 1*123**3
    f = a + b
    if f % 123 == 0 :
        print(f//123)


print('NEXT task ')
n = 5*216**1256 - 5*36**1146 + 4*6**1053 - 1087
base = 6
lst = []
while n > 0:
    lst.append(n%base)
    n = n // base
print(sum(lst), 'qwerty')


print('NEXT task ')
k = 0
for x in range(0, 1000):
    if (x%10 == 5) and (len(hex(x)[2:]) < 9) and (len(oct(x)[2:]) > 10):
        k += 1
print(k)

print(len(hex(123456)[2:]))


# Дано выражение:
# 10х56₃₀ + 21х11₂₄
# Найдите максимальное х, при котором значение выражения кратно 7,
# в ответ укажите х - его численное значение.
print('NEXT task ')
st = '0123456789ABCDEFGHIGKLMN'
for x in st :
    a = int(f'10{x}56', 30)
    b = int(f'21{x}11', 24)
    f = a + b
    if f % 7 == 0:
        print(x)



"""
14. Значение выражения 9**12 + 3**8 − 3? записали в системе счисления с основанием 3.
Сколько цифр 2 содержится в этой записи?

"""

a = 9**12 + 3**8 - 3
print(a)
base = 3
l = []
while a > 0:
    l.append(a%3)
    a //= 3

l = l[::-1]
print(l.count(2))


def p(x, base):
    ans = ''
    while x > 0:
        ans += str(x%base)
        x = x//base
    return ans[::-1]

# st = '0123456789ABCDEFGHIJKLMNOPQ'
# for x in st:
#     f = int('123{}24'.format(x), 27) + int('{}178'.format(x), 27)
#     if f % 26 == 0:
#         print(x, f//26)


st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0
n = 3*2187**2020+3*729**2021-2*81**2022+27**2023-4*3**2024-2029
lst = []
base = 27
while n > 0:
    lst.append(n%base)
    n //= base
print(lst)
ans = 0
for el in lst:
    if el > 9:
        ans += 1
print(ans)
# def summa(x):
#     ans = 0
#     while x != '':
#         ans += int(x[-1])
#         x = x[:-1]
#     return ans
#
# print(summa(s))

st = '0123456789ABC'
for x in st:
    f = int('753{}2'.format(x), 13) + int('2{}173'.format(x), 13)
    if f % 12 == 0:
        print(x, f//12)