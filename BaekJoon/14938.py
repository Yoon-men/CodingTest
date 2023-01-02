# 백준14938 : 서강그라운드
import sys; input = sys.stdin.readline

def FW_joyGo(graph) : 
    for i in range(n) : 
        for j in range(n) : 
            for k in range(n) : 
                if graph[j][k] > graph[j][i] + graph[i][k] : 
                    graph[j][k] = graph[j][i] + graph[i][k]

    return graph


if __name__ == "__main__" : 
    n, m, r = map(int, input().split())
    itemLi = list(map(int, input().split()))
    graph = [[sys.maxsize] * n for _ in range(n)]
    for i in range(r) : 
        a, b, l = map(int, input().split())
        graph[a-1][b-1] = l
        graph[b-1][a-1] = l

    graph = FW_joyGo(graph)
    for i in range(n) : 
        graph[i][i] = 0

    ansLi = []
    for i in range(n) : 
        tmp = 0
        for j in range(n) : 
            if graph[i][j] <= m : 
                tmp += itemLi[j]
        ansLi.append(tmp)

    print(max(ansLi))