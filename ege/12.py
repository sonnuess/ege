"""
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 85 идущих подряд цифр 9? В ответе запишите полученную строку.
НАЧАЛО
ПОКА нашлось (666) или нашлось (999)
   ЕСЛИ нашлось (666)
      ТО заменить (666, 9)
      ИНАЧЕ заменить (999, 6)
   КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
"""

st = '9' * 85

while '666' in st or '999' in st:
    if '666' in st:
        st = st.replace('666', '9', 1)
    else:
        st = st.replace('999', '6', 1)

print(st)
# 699

"""
"""

for n in range(4, 10000):
    st = '8' + '4' * n
    while '4444' in st or '844' in st or '84' in st:
        if '4444' in st:
            st = st.replace('4444', '884', 1)
        if '844' in st:
            st = st.replace('844', '488', 1)
        if '84' in st:
            st = st.replace('84', '3343', 1)

    if len(st) >= 20:
        print(n)

print(n)
# 9999

"""
Дана программа для Редактора:
НАЧАЛО
ПОКА нашлось (52) ИЛИ нашлось (2222) ИЛИ нашлось (1112)
    ЕСЛИ нашлось (52)
        заменить (52, 11)
        заменить (2222, 5)
    ИНАЧЕ
        заменить (1112, 2)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой выше программе поступает строка, начинающаяся с цифры «5», а затем содержащая n цифр «2» (3 < n < 10 000).
Определите наибольшее значение n, при котором сумма цифр в строке, получившейся в результате выполнения программы, равна 1685.
"""


def summa(x):
    s = 0
    for i in str(x):
        s += int(i)
    return int(s)


for n in range(4, 10000):
    st = '5' + '2' * n
    while '52' in st or '2222' in st or '1112' in st:
        if '52' in st:
            st = st.replace('52', '11', 1)
        if '2222' in st:
            st = st.replace('2222', '5', 1)
        if '1112' in st:
            st = st.replace('1112', '2', 1)

    if summa(st) == 1685:
        print(n)
# 4200

"""
НАЧАЛО
   ПОКА нашлось(123)
      заменить(12,3)
   КОНЕЦ ПОКА
КОНЕЦ
Сколько троек будет содержать строка, которая получится в результате применения приведённой выше программы к строке, состоящей из 30   идущих подряд чисел 123  ?
В ответе запишите только число – количество троек в полученной строке.
"""
st = '123' * 30

while '123' in st:
    st = st.replace('12', '3', 1)

print(st.count('3'))

# 60

"""
НАЧАЛО
   ПОКА нашлось(LL)
      заменить(BU, LL)
      ЕСЛИ НЕ нашлось(BULL)
      заменить(LLLLLL, CAT)
   КОНЕЦ ПОКА
КОНЕЦ
Алгоритм выше превращает быков (BULL) в милых котиков (CAT). При этом котики боятся быков, поэтому пока есть хотя бы один бык котик появляться не будет.
Сколько раз алгоритм сделает команду заменить, если в итоге должно получиться ровно два котика?
"""
for n in range(1, 100):
    c = 0
    st = 'BULL' * n
    flag = False
    while 'LL' in st:
        if 'BU' in st:
            st = st.replace('BU', 'LL', 1)
            c += 1
        if 'BULL' not in st:
            st = st.replace('LLLLLL', 'CAT', 1)
            c += 1
        if st.count('LL') == len(st) or c > 1000:
            break
    if st.count('CAT') == 2:
        print(c)
        break
# 5


"""
Цикл
   ПОКА условие
      последовательность команд
   КОНЕЦ ПОКА
выполняется, пока условие истинно.
Дана программа для редактора:
НАЧАЛО
   ПОКА нашлось(12)
      заменить(12,2)
      заменить(23,3)
   КОНЕЦ ПОКА
КОНЕЦ
В результате работы программы к строке  получилась строка, в которой содержится 35   цифр     2  . Сколько цифр 2   было в изначальной строке?
"""
st = ''
while '12' in st:
    st = st.replace('12', '2', 1)
    st = st.replace('23', '3', 1)

''''''''''''''''''''''''''
st = '8' * 45
while '1111' in st or '8888' in st:
    if '1111' in st:
        st = st.replace('1111', '88', 1)
    else:
        st = st.replace('8888', '11', 1)

print(st)

def summa(x):
    ans = 0
    while x != '':
        ans += int(x[-1])
        x = x[:-1]
    return ans

ans = 0
for n in range(3, 10001):
    st = '2' + '5' * n
    while '25' in st or '355' in st or '555' in st:
        if '25' in st:
            st = st.replace('25', '5', 1)
        if '355' in st:
            st = st.replace('355', '52', 1)
        if '555' in st:
            st = st.replace('555', '3', 1)
    if st.count('3') == 3:
        print(n)
        break
print(ans)




def summa(x):
    ans = 0
    while x != '':
        ans += int(x[-1])
        x = x[:-1]
    return ans

ans = 0
for n in range(3, 10001):
    st = '5' + '2' * n
    while '52' in st or '2222' in st or '1122' in st:
        if '52' in st:
            st = st.replace('52', '11', 1)
        if '2222' in st:
            st = st.replace('2222', '5', 1)
        if '1122' in st:
            st = st.replace('1122', '25', 1)
    if summa(st) == 64:
        print(n)
print(ans)


def summa(x):
    ans = 0
    while x != '':
        ans += int(x[-1])
        x = x[:-1]
    return ans
ans = 0
for n in range(3, 10000):
    st = '1' + '2' * n
    while '12' in st or '322' in st or '222' in st:
        if '12' in st:
            st = st.replace('12', '2', 1)
        if '322' in st:
            st = st.replace('322', '21', 1)
        if '222' in st:
            st = st.replace('222', '3', 1)
    ans = max(summa(st), ans)

print(ans)



