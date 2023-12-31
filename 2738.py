A,B=[],[]
N,M=map(int,input().split())

for i in range(N):
    a=list(map(int,input().split()))
    A.append(a)
for j in range(N):
    a=list(map(int,input().split()))
    B.append(a)

for q in range(N):
    for w in range(M):
        print(A[q][w]+B[q][w], end=" ")
    print()



