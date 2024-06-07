def F(n):
    if n == 1:
        return 1
    if n > 1 and n % 2 == 0:
        return n*n + F(n-1)
    if n > 1 and n % 2 != 0:
        return F(n-1) + 2*F(n-2)

print(F(23))


def F(n):
    if n == 0:
        return 0
    if n > 0 and n%2 == 0:
        return F(n/2)
    if n % 2 != 0:
        return F(n-1) + 1


c = 0
for n in range(1, 501):
    if F(n) == 8:
        c += 1
print(c) #5



def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + F(n + 3)


print(F(23) - F(21)) # 1338



def F(n):
    if n > 15:
        return n * n + n * 2
    if n <= 15:
        return F(n + 2) + 2 * F(n + 1)
c = 0
for n in range(1, 1001):
    if F(n)%5 == 0:
        c += 1

print(c) #394


def F(n):
    if n < 12:
        return n
    if (n > 11) and (n%2 == 0):
        return G(n//2) * 2 - F(n - 1)
    if (n > 11) and (n%2 == 1):
        return -G(n - 1)

def G(n):
    if (n < 12) and (n%3 != 0):
        return F(n - 1) + n
    elif (n < 12) and (n%3 == 0):
        return G(n - 1) + F(n//3) - n
    else:
        return n * n

for n in range(1, 1001):
    sm = 0
    a = abs(F(n))
    for i in range(len(str(a))):
        sm += a % 10
        a //= 10
    if sm == 33:
        print(n)