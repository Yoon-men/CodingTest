# 백준1916 : 최소비용 구하기
from heapq import heappush, heappop
import sys ; input = sys.stdin.readline

def joyGo(startJoyGo) : 
    hq = []
    heappush(hq, (0, startJoyGo))
    visited[startJoyGo] = 0

    while hq : 
        p, d = heappop(hq)      # pay, departure
        if visited[d] < p : continue

        for endJoyGo, pay in graph[d] : 
            totalPay = p + pay

            if visited[endJoyGo] > totalPay : 
                heappush(hq, (totalPay, endJoyGo))
                visited[endJoyGo] = totalPay

if __name__ == "__main__" : 
    N = int(input())
    visited = [sys.maxsize] * (N+1)

    graph = [[] for _ in range(N+1)]
    for _ in range(int(input())) : 
        s, e, p = map(int, input().split())     # start, end, pay
        graph[s].append((e, p))
    departure, arrival = map(int, input().split())

    joyGo(departure)
    print(visited[arrival])