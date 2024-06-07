print((bin(112)[2:]), (bin(208)[2:]), (bin(0)[2:]), (bin(0)[2:]))
print((bin(255)[2:]), (bin(255)[2:]), (bin(128)[2:]), (bin(0)[2:]))

cnt = 0
# 01110000 11010000 00000000 00000000
# 11111111 11111111 10000000 00000000

for b1 in '01':
    for b2 in '01':
        for b3 in '01':
            for b4 in '01':
                for b5 in '01':
                    for b6 in '01':
                        for b7 in '01':
                            for b8 in '01':
                                for b9 in '01':
                                    for b10 in '01':
                                        for b11 in '01':
                                            for b12 in '01':
                                                for b13 in '01':
                                                    for b14 in '01':
                                                        for b15 in '01':
                                                                    ip_k = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12 + b13 + b14 + b15
                                                                    ip = ip_k + "01110000 11010000 0"
                                                                    if ip.count('1') % 11 == 0:
                                                                        cnt += 1
print(cnt) #3003

print((bin(184)[2:]), (bin(170)[2:]), (bin(54)[2:]), (bin(144)[2:]))
print((bin(255)[2:]), (bin(255)[2:]), (bin(255)[2:]), (bin(240)[2:]))

cnt = 0
# 10111000 10101010 00110110 10010000 ip
# 11111111 11111111 11111111 11110000 mask

for b1 in '01':
    for b2 in '01':
        for b3 in '01':
            for b4 in '01':
                ip_k = b1 + b2 + b3 + b4
                ip = '10111000 10101010 00110110 1001' + ip_k
                if '111' in ip:
                    cnt += 1
print(cnt)



print((bin(154)[2:]), (bin(233)[2:]), (bin(0)[2:]), (bin(0)[2:]))
print((bin(255)[2:]), (bin(255)[2:]), (bin(0)[2:]), (bin(0)[2:]))

cnt = 0

# 10011010 11101001 00000000 00000000
# 11111111 11111111 00000000 00000000
for b1 in '01':
    for b2 in '01':
        for b3 in '01':
            for b4 in '01':
                for b5 in '01':
                    for b6 in '01':
                        for b7 in '01':
                            for b8 in '01':
                                for b9 in '01':
                                    for b10 in '01':
                                        for b11 in '01':
                                            for b12 in '01':
                                                for b13 in '01':
                                                    for b14 in '01':
                                                        for b15 in '01':
                                                            for b16 in '01':
                                                                ip = '10011010 11101001' + b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12 + b13 + b14 + b15 + b16
                                                                if ip[-1] == '0':
                                                                    cnt += 1
print(cnt)


print((bin(202)[2:]), (bin(75)[2:]), (bin(38)[2:]), (bin(152)[2:]))
print((bin(255)[2:]), (bin(255)[2:]), (bin(255)[2:]), (bin(248)[2:]))

cnt = 0

# 11001010 01001011 00100110 10011000
# 11111111 11111111 11111111 11111000
for b1 in '01':
    for b2 in '01':
        for b3 in '01':
            ip = '10011010 11101001' + b1 + b2 + b3
            if '111' in ip:
                cnt += 1
print(cnt)

print((bin(122)[2:]), (bin(159)[2:]), (bin(136)[2:]), (bin(144)[2:]))
print((bin(255)[2:]), (bin(255)[2:]), (bin(255)[2:]), (bin(248)[2:]))

cnt = 0

# 01111010 10011111 10001000 10010000
# 11111111 11111111 11111111 11111000
for b1 in '01':
    for b2 in '01':
        for b3 in '01':
                ip = '01111010 10011111 10001000 10010' + b1 + b2 + b3
                if ip.count('1') % 4 != 0:
                    cnt += 1
print(cnt)
