N=int(input())

a=list(map(int,input().split()))

c=int(input())
d=0
for i in a:
     if i==c:
        d+=1
        
print(d)