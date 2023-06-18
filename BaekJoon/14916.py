# 백준14916 : 거스름돈
def joyGo(n: int) : 
    cnt = 0
    while n > 0 : 
        if n % 5 == 0 : 
            cnt += n//5
            return cnt
        else : 
            n -= 2
            cnt += 1

    return cnt if n >= 0 else -1


if __name__ == "__main__" : 
    print(joyGo(int(input())))