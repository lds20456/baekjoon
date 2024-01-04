N = int(input())
score = list(map(int, input().split()))

M = 0
for i in score:
    if i > M:
        M = i

s = 0
for i in score:
    s += i / M * 100

aver = s / N

print(aver)

