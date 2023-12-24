A=int(input())
B=int(input())
C=int(input())
T=A*B*C

dic=str(T)

for i in range(10):
    n=dic.count(str(i))
    print(n)

       