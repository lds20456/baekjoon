T=int(input())

for i in range(T):
    H,W,N=map(int,input().split())
    b=N//H
    c=N%H

    if c==0:
        print((H*100)+b)
    else:
        print((c*100)+(b+1))
    