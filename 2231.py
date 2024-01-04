N = int(input()) 
a = 0
  
for i in range(1, N + 1):
    now = i
    s = now 

    b = 0
    c = now
    for _ in range(len(str(now))):
        b += c % 10
        c //= 10
    
    s += b

    if s == N:  
        a = i  
        break  

print(a)
