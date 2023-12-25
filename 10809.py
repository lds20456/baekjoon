s=input()
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in a:
    for j in range(len(s)):
        if s[j]==i:
            print(j, end=" ")
            break
    if i not in s:
        print(-1, end=" ")







