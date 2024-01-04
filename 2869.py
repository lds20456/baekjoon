A, B, V=map(int, input().split())

a=(V - B)//(A - B)
if (V - B)%(A - B)!=0:
    a+=1

print(a)
