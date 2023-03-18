# 백준1015 : 수열 정렬
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> list : 
    sortedLi = sorted(Li)
    ansLi = [0] * len(Li)
    for i in range(len(Li)) : 
        idx = sortedLi.index(Li[i])
        ansLi[i] = idx
        sortedLi[idx] = -1

    return ansLi


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))

    print(*joyGo(Li))