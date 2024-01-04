N = int(input())
a = list(map(int, input().split()))

count = 0
for i in a:
    if i>=2:  
        p=1
        for j in range(2, i):  
            if i % j == 0:
                p=0
                break
        count+=p 

print(count)
