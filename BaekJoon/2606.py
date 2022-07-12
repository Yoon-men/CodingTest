# 백준2606 : 바이러스
import sys
input = sys.stdin.readline


def check(origin) : 
    global cnt
    visited[origin-1] = 1
    for i in coms[origin-1] : 
        if visited[i-1] == 0 : 
            check(i)
            cnt += 1


if __name__ == "__main__" : 
    N = int(input())
    coms = [[] for _ in range(N)]
    for _ in range(int(input())) : 
        comA, comB = map(int, input().split())
        coms[comA-1].append(comB)
        coms[comB-1].append(comA)

    visited = [0] * N
    cnt = 0
    check(1)
    print(cnt)