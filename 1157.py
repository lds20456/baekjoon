a=input()
a=a.upper()
c={} #카운트 딕셔너리

for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1

mc=0 #많이나온 알파벳 횟수 카운트
for i in c:
    count=c[i]
    if count>mc:
        mc=count

ma=[] #많이나온 알파벳 저장하는 리스트
for i in c:
    if c[i]==mc:
        ma.append(i)
    
if len(ma)==1:
    print(ma[0])
else:
    print("?")



