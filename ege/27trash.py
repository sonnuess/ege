f = open('text.txt').read().split('\n')
f = list(map(int, f))
N = 110
N_p = 55
costs = [0] * len(f)
for i in range(len(f)):
    costs[0] += f[i] * min(i, (len(f) - i))

p_sum = [0] * len(f)

for i in range(len(f)):
    for j in range(i, i+(len(f)//2)):
        p_sum[i] += f[j % len(f)]

print(p_sum)

sm = sum(f)
for i in range(1, len(f)):
    costs[i] = costs[i-1] + sm - 2*p_sum[i]

print(min(costs))

# 96


f = open('file.txt').read().split('\n')
f = list(map(int, f))
N = 20
costs = [0] * len(f)
for i in range(len(f)):
    costs[0] += f[i] * min(i, (len(f) - i))

p_sum = [0] * len(f)

for i in range(len(f)//2):
    p_sum[0] += f[i]

for i in range(1, len(f)):
    p_sum[i] = p_sum[i - 1] - f[i-1] + f[(i + (len(f)//2) - 1) % len(f)]

sm = sum(f)
for i in range(1, len(f)):
    costs[i] = costs[i-1] + sm - 2*p_sum[i]
sr = 100000000000000000000000000000000
ans = 0
for i in range(len(costs)):
    if costs[i] < sr:
        ans = i+1
        sr = costs[i]
print(ans)
# 8 41495