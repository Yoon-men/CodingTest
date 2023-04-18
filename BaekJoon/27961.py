# 백준27961 : 고양이는 많을수록 좋다
def joyGo(N: int) -> None : 
    if not N : print(0); return
    tmp = 0
    while 2**tmp < N : 
        tmp += 1
    print(tmp+1)

if __name__ == "__main__" : 
    N = int(input())
    joyGo(N)