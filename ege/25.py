
'''
Найти на промежутке [157314,853412]  числа, которые являются квадратами простых чисел. В ответе запишите количество таких чисел и их сумму через пробел.
'''
def is_prime(x):
    for i in range(2, round(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
k = 0
sm = 0
for x in range(157314,853413):
    if (x**0.5)%1 == 0:
        if is_prime(x**0.5) == True:
            k += 1
            sm += x

print(k)
print(sm)



'''
Найдите наибольшее натуральное число на отрезке [10000;5000000]  , которое имеет ровно 10   делителей. В ответе укажите число.'''

def divisors(x):
    cnt = 0
    for d in range(1, round(x**0.5) + 1):
        if x % d == 0:
            cnt += 1
            if d != (x//d): # 3 != 9//3 - false
                cnt += 1
    return cnt

c = 0
for x in range(5000000, 10000, -1):
    if divisors(x) == 10:
        print(x)
#4999563


'''
Найдите все натуральные числа, принадлежащие отрезку [11 111 111; 77 777 777], у которых ровно 5   различных делителей. В ответе укажите количество данных чисел.
'''

def divisors(x):
    cnt = 0
    for d in range(1, round(x**0.5) + 1):
        if x % d == 0:
            cnt += 1
            if d != (x//d): # 3 != 9//3 - false
                cnt += 1
        if cnt == 6:
            break
    return cnt

c = 0
for x in range(11111111, 77777778):
    if (x**0.5)%1 == 0:
        if divisors(x) == 5:
            c += 1

print(c)
#8

'''
Определите количество составных натуральных чисел из диапазона [3;30000]  , у которых количество нетривиальных делителей не менее трех.
'''
def divisors(x):
    cnt = 0
    for d in range(2, round(x**0.5) + 1):
        if x % d == 0:
            cnt += 1
            if d != (x//d): # 3 != 9//3 - false
                cnt += 1
    return cnt

c = 0
for x in range(3, 30001):
    if divisors(x) > 2:
        c += 1

print(c)
#19282


'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [28916485;49716586]  ,
 числа, имеющие ровно 5   делителей, оканчивающихся на 0  или 5  . В ответ запишите все найденные числа через пробел в порядке возрастания.
'''

# def divisors(x):
#     cnt = 0
#     for d in range(1, round(x**0.5) + 1):
#         if x % d == 0 :
#             if (d%10 == 5 or d%10 == 0):
#                 cnt += 1
#             if d != (x//d) and ((x//d)%10 == 5 or (x//d)%10 == 0):
#                 cnt += 1
#         if cnt == 6:
#             break
#     return cnt
#
# k = 0
# for x in range(28916485, 49716587, 5):
#     if divisors(x) == 5:
#         k += 1
#         print(x)
#


def is_prime(x):
    for i in range(2, round(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def summa(x):
    sum_digits = 0
    for i in str(x):
        sum_digits += int(i)
    return sum_digits

s = 0
for x in range(131590, 591585):
    if is_prime(x) == True:
        s += summa(x)

print(s)

''''''''''''
def divisors(x):
    cnt = 0
    for d in range(1, round(x**0.5) + 1):
        if x % d == 0 :
            cnt += 1
            if x//d != d :
                cnt +=1
    return cnt


c = 0
for x in range(1111, 555556):
    if divisors(x)%2 == 0 :
        c += 1

print(c)

''''''''''''''''''

def divisors(x):
    cnt = 0
    for d in range(1, round(x**0.5) + 1):
        if x % d == 0 :
            cnt += 1
            if x//d != d :
                cnt +=1
    return cnt

mx = 0
mx_d = 1
for x in range(111111, 777778):
    if divisors(x) > mx_d:
        mx_d = divisors(x)
        mx = max(mx, x)

print(mx)

''''''''''''''''''
def divisors(x):
    cnt = 0
    for d in range(1, round(x**0.5) + 1):
        if x % d == 0 :
            cnt += 1
            if x//d != d :
                cnt +=1
    return cnt

# x = 1
# while divisors(x) != 256:
#     x += 1
# print(x)

print(divisors(1081080))


''''''''
def divisors(x):
    cnt = 0
    for d in range(1, round(x**0.5) + 1):
        if x % d == 0 :
            cnt += 1
            if x//d != d :
                cnt +=1
    return cnt


c = 0
for x in range(100010,321342):
    if divisors(x) == 5:
        c += 1

print(c)


# def divisors(x):
#     cnt = 0
#     for d in range(1, round(x**0.5) + 1):
#         if x % d == 0 :
#             if d % 2 == 0:
#                 cnt += 1
#             if x//d != d:
#                 if (x//d)%2 == 0:
#                     cnt +=1
#         if cnt == 4:
#             break
#     return cnt
#
#
# c = 0
# for x in range(101000000, 102000001):
#     if divisors(x) == 3:
#         print(x)
#
# print(c)