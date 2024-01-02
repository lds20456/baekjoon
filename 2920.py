a=list(map(int,input().split()))
b=0

for i in range(len(a)-1):
    if a[i]+1==a[i+1]:
        b=1
    elif a[i]-1==a[i+1]:
        b=2
    else:
        b=0
        break

if b==0:
    print("mixed")
elif b==1:
    print("ascending")
elif b==2:
    print("descending")

