# Дарья составляет пятибуквенные слова из букв слова УСПЕХ, причем известно, что буквы в словах могут повторяться любое количество раз или же не встречаться вовсе.
# Помогите Дарье найти количество различных слов, являющимися палиндромами и содержащими в середине гласную букву.
a = 'успех'
word = list(a)
c = 0
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    w = b1 + b2 + b3 + b4 + b5
                    if (w == w[::-1]) and (w[2] == 'у' or w[2] == 'е'):
                        c +=1
                        print(w)
print(c)
#50


'петя составляет слова, состоящие из 6 букв, из символов С, О, Н. '
'В каждом слове есть хотя бы две буквы Н и нет сочетания НС. Каждая буква может встречаться любое количество раз. Сколько слов может составить Петя?'
a = 'сон'
word = list(a)
c = 0
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    for b6 in word:
                        w = b1 + b2 + b3 + b4 + b5 + b6
                        if w.count('н') >= 2 and 'нс' not in w:
                            c +=1
                            print(w)
print(c)

'Каждый день Матвей составляет задачки из букв П, Л, А, Н, И, М, Е, Т, Р, И, Я.'
'Сколько различных 5-значных слов он может составить, если каждую согласную букву он должен использовать нечётное количество раз'

a = 'планиметря'
s = 'плнмтр'
word = list(a)
k = 0
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    w = b1 + b2 + b3 + b4 + b5
                    c = True
                    for el in s:
                        if w.count(el) % 2 == 0 and w.count(el) != 0:
                            c = False
                    if c == True:
                        k += 1
print(k)
#59590


a = 'trja'
word = list(a)
c = 0
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                c += 1
                w = b1 + b2 + b3
                if w == 'сон':
                    print(c)
                if w == 'нос':
                    print(c)
print(20-12-1)  #7

''''''''''''''
a = 'екмопртью'
word = list(a)
c = 0
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    c += 1
                    w = b1 + b2 + b3 + b4 + b5

                    if (w[0] != 'ь') and (w.count('к') == 2):
                        print(c)
                        print(w)
#58979

##
a = 'агмнсту'
word = list(a)
c = 0
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    for b6 in word:
                        c += 1
                        w = b1 + b2 + b3 + b4 + b5 + b6
                        if (w[0] != 'у') and (w.count('м') == 2) and (w.count('г') < 2):
                            print(c)
                            print(w)
#100810


'''
Все 5-буквенные слова, в составе которых могут быть буквы К, А, М, Е, О записаны в определённом порядке и пронумерованы, начиная с 1. Ниже приведено начало списка.
ККККК
ККККА
ККККМ
ККККЕ
ККККО
КККАК
…
Сколько слов, оканчивающихся на ОМ, между словами «КОМОК» и «ЕМКОМ»?
'''

a = 'камео'
word = list(a)
c = 0
l = []
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    c += 1
                    w = b1 + b2 + b3 + b4 + b5
                    l.append(w)
print(l)
print(l.index('комок'))
print(l.index('емком'))

#570 2147
k = 0
for i in range(571, 2147):
    if l[i][3:] == 'ом':
        k += 1

print(k)
#63

a = '0123456789abcdef'
n = '02468ace'
ch = '13579bdf'
c = 0
word = list(a)
for b1 in word:
    for b2 in word:
        for b3 in word:
            if (b1 != b2) and (b2 != b3) and (b1 != b3):
                if ((b1 in n) and (b3 in n) and (b2 in ch)) or ((b1 in ch) and (b2 in n) and (b3 in ch)):
                    if b1 != '0':
                        c += 1
print(c)
#896



'''
Сколько слов из шести символов может составить Петя перестановкой букв слова БАОБАБ?
'''
#60
a = 'баобаб'
word = list(a)
l = []
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    for b6 in word:
                        w = b1 + b2 + b3 + b4 + b5 + b6
                        if w not in l and (w.count('б') == 3)  and (w.count('а') == 2) and (w.count('о') == 1):
                            l.append(w)

print(len(l))
#60


'''
Азат составляет 5-буквенные слова из букв Д, Е, М, О, Н,
 причём если слово начинается на гласную, то оно обязательно должно оканчиваться на согласную.
 Все буквы используются ровно один раз. Сколько слов может составить Азат?
'''
a = 'демон'
с = 0
word = list(a)
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    w = b1 + b2 + b3 + b4 + b5
                    if ((b1 in 'ео ' and b5 in 'дмн') or (b1 in 'дмн')) and w.count('д') == 1 and w.count('е') == 1 and w.count('м') == 1 and w.count('о') == 1 and w.count('н') == 1:
                        с += 1
print(с)
#108

'''
Лиза составляет 5-буквенные слова из букв Ц, И, Ф, Р, А. Каждая из букв может встречаться в слове сколько угодно раз или не встречаться совсем,
 причём слово не может начинаться с гласной. Сколько различных слов может составить Лиза?
'''
a = 'цифра'
с = 0
word = list(a)
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                for b5 in word:
                    w = b1 + b2 + b3 + b4 + b5
                    if b1 not in 'иа':
                        с += 1
print(с)
#1875

'''
Сколько слов можно составить из букв С, Т, О, Л, если каждое слово состоит из четырёх букв и в каждом слове есть по крайней мере одна буква О??
'''
a = 'стол'
с = 0
word = list(a)
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                w = b1 + b2 + b3 + b4
                if w.count('о') >= 1:
                    с += 1
print(с)
#175

'''
АНАСТАСИЯ из букв своего имени составляет слова перестановкой исходных букв. Сколько различных слов может составить АНАСТАСИЯ, если первая буква не может быть согласной?
'''

s = 'АНТСИЯ'
count = 0
for b1 in s:
    for b2 in s:
        for b3 in s:
            for b4 in s:
                for b5 in s:
                    for b6 in s:
                        for b7 in s:
                            for b8 in s:
                                for b9 in s:
                                    f = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9
                                    a = f.count('А') == 3
                                    n = f.count('Н') == 1
                                    c = f.count('С') == 2
                                    t = f.count('Т') == 1
                                    i = f.count('И') == 1
                                    y = f.count('Я') == 1
                                    if a and n and c and t and t and i and y and f[0] not in 'НСТ':
                                        count += 1
print(count)
#16800

'''
Сколько слов можно составить из букв С, Т, О, Л, если каждое слово состоит из четырёх букв и в каждом слове есть по крайней мере одна буква О??
'''
a = 'стол'
с = 0
word = list(a)
for b1 in word:
    for b2 in word:
        for b3 in word:
            for b4 in word:
                w = b1 + b2 + b3 + b4
                if w.count('о') >= 1:
                    с += 1
print(с)

st = '0123456'
m = '0246'
c = 0
for b1 in st:
    for b2 in st:
        for b3 in st:
            for b4 in st:
                for b5 in st:
                    for b6 in st:
                        for b7 in st:
                            counter = 0
                            s = b1 + b2 + b3 + b4 + b5 + b6 + b7
                            for el in s:
                                if el in m:
                                    counter += 1
                            if (b1 != '0') and (counter == 2):
                                c += 1
print(c)


st = '012345678'
c = 0
for b1 in st:
    for b2 in st:
        for b3 in st:
            for b4 in st:
                for b5 in st:
                    counter = 0
                    s = b1 + b2 + b3 + b4 + b5
                    for i in range(len(s)-1):
                        if s[i] == s[i+1]:
                            counter = 1
                    if (b1 != '0') and (counter == 0) and s.count('5') == 1:
                        c += 1
print(c)



st = '012345'
c = 0
n = '135'
for b1 in st:
    for b2 in st:
        for b3 in st:
            for b4 in st:
                for b5 in st:
                    for b6 in st:
                        counter = 0
                        s = b1 + b2 + b3 + b4 + b5 + b6
                        for i in range(len(s) - 1):
                            if (s[i] in n) and (s[i+1] == '2') or (s[i+1] in n) and (s[i] == '2'):
                                counter = 1
                        if (b1 != '0') and (counter == 0) and s.count('2') == 1:
                            c += 1
print(c)
