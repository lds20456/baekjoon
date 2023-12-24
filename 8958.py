a=int(input())

for i in range(a):
    tscore=0 #총점수
    score=0 #라운드 점수
    b=input()
    for j in b:
        if j=='O':
            score += 1
            tscore += score
        else:
            score = 0
    print(tscore)


