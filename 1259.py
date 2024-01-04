while True:
    a = input()
    if a =='0':
        break

    b = len(a)
    pl = 1
    for i in range(b // 2):
        if a[i] != a[b - i - 1]:
            pl = 0
            break
    
    if pl:
        print("yes")
    else:
        print("no")
