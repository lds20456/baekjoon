b=[]
c=[]
for i in range(10):
    a=int(input())
    b.append(a%42)

for j in b:
    if j not in c:
        c.append(j)

print(len(c))