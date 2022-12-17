# 백준5341 : Pyramids
def joyGo(n) : 
    if n == 1 : 
        return 1
    elif n >= 2 : 
        return joyGo(n-1) + n

if __name__ == "__main__" : 
    while True : 
        N = int(input())
        if not N : break
        print(joyGo(N))