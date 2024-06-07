# На числовой прямой даны два отрезка:
# M = [4, 36] и N = [11, 24].
# Укажите наибольшую возможную длину такого отрезка A, что формула:
# f = (x ∈ A) →  ¬((x ∈ M) ≡ (x ∈ N))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной .

M = [x for x in range(40,371)]
N = [x for x in range(110, 241)]
A = [x for x in range(40, 371)]

for x in range(40, 371):
    f = (x in A) <= (not((x in M) == (x in N)))
    if f == False:
        A.remove(x)

print(A)
#[4, 11) 7
#(24, 37] 13

M = [x for x in range(40, 361)]
N = [x for x in range(110, 241)]
A = [x for x in range(40, 361)]


for x in range(40,361):
    f = (x in A) <=  (not((x in M) == (x in N)))
    if f == False:
        A.remove(x)
print(A)

#[4, 11)
#(24,36]
M = [x for x in range(40, 361)]
N = [x for x in range(110, 241)]
A = [x for x in range(40, 361)]

''''''''''' other
'''''''''''
for x in range(40,361):
    f = (x in A) <=  (not((x in M) == (x in N)))
    if f == False:
        A.remove(x)
print(A)

#[4, 11)
#(24,36]

"""""
На числовой прямой даны два отрезка: P = [20, 50] и Q = [30,65]. Отрезок A таков, что форму‐
ла
¬(x ∈ A) → ((x ∈ P) →¬ (x ∈ Q))
истинна при любом значении переменной x. Какова наименьшая возможная длина отрезка A?
"""
P = [x/10 for x in range(200, 501)]
Q = [x/10 for x in range(300, 651)]
A = []

for x in range(20,66):
    f = (x not in A) <= ((x in P) <= (x not in Q))
    if f == False:
        A.append(x)

print(len(A))