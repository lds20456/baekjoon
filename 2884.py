H, M = map(int, input().split())

#H=int(input())
#M=int(input()) 
#45분을M에서 빼야되 근데 if M>=44면 그냥 빼면되는거야
#근데 if M<45면 H에 변화가 생기잖아 그러면 H에서도 1을 빼고, 남은 M을 빼야지? 근데 H가 0이면 -1로
#가니까 저기에 M<45 이고(and조건) H>0 이게 elif에 들가면 된다!
#근데 만약에 H가 0이면 어떡해? 그럼 딴거 필요없이 그냥 23시잖아 그치?

if M>=45:
    print(H, M-45)
elif M<45 and H>0:
    print(H-1, M+15)
else:
    print(23, M+15)

