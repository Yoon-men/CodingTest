# 백준4375 : 1
while True : 
    try : n = int(input())
    except : break
    m = 1
    while True : 
        if m % n == 0 : 
            print(len(str(m)))
            break
        m = m*10 + 1