# 백준2467 : 용액
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list) -> list : 
    s, e = 0, N-1
    total = sys.maxsize
    ans_list = []

    while s < e : 
        a, b = Li[s], Li[e]
        tmp = a + b
        if abs(tmp) < total : 
            total = abs(tmp)
            ans_list = [a, b]
        if tmp <= 0 : s += 1
        else : e -= 1
    
    return ans_list


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))
    print(*(joyGo(N, Li)))