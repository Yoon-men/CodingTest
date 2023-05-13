# 백준2473 : 세 용액
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list) -> list : 
    Li.sort()
    total = sys.maxsize
    ans_list = []

    for i in range(N-2) : 
        s, e = i+1, N-1
        while s < e : 
            a, b, c = Li[i], Li[s], Li[e]
            tmp = a + b + c
            if abs(tmp) < total : 
                total = abs(tmp)
                ans_list = [a, b, c]
            if tmp < 0 : s += 1
            else : e -= 1
    
    return ans_list


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))
    print(*joyGo(N, Li))