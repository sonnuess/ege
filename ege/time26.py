'ФИЛЬМЫ КОЛИЧЕСТВО'
films = open('file.txt').read().split('\n')
for i in range(len(films)):
    films[i] = list(map(int, films[i].split()))
ans = 0
c = 0
flag = 0
for t in range(1,1000):
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