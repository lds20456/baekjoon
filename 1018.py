N,M=map(int,input().split())
bd=[]
for i in range(N):
    a=input()
    bd.append(a)
max=64
for j in range(N-7):
    for k in range(M-7):
        for s in ["W", "B"]:
            count=0
            for l in range(j,j+8):
                for n in range(k,k+8):
                    now=bd[l][n]
                    if (l-j+n-k)%2==0:  
                        if now!=s:
                            count+=1
                    else:
                        if now==s:
                            count+=1        
                          
        if count<max:
            max=count
        if 64-count<max:
            max=64-count
print(max)
        
