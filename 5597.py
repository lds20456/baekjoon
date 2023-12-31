s=[]

for i in range(28):
    a=int(input())
    s.append(a)

for i in range(1,31):
    if i not in s:
        print(i)