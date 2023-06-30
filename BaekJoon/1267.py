# 백준1267 : 핸드폰 요금
import sys; input = sys.stdin.readline

def joyGo(Li: list) : 
    Y_total, M_total = 0, 0
    for t in Li : 
        Y_total += 10 * (t//30+1)
        M_total += 15 * (t//60+1)
    
    return ["Y M" if Y_total == M_total else 'Y' if Y_total < M_total else 'M', Y_total if Y_total <= M_total else M_total]


if __name__ == "__main__" : 
    _ = int(input())
    Li = list(map(int, input().split()))

    print(*joyGo(Li))