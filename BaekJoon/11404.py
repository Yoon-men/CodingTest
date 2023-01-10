# 백준11404 : 플로이드
import sys; input = sys.stdin.readline

def FW_joyGo(graph) : 
    for i in range(n) : 
        for j in range(n) : 
            for k in range(n) : 
                if graph[j][k] > graph[j][i] + graph[i][k] : 
                    graph[j][k] = graph[j][i] + graph[i][k]

    return graph


if __name__ == "__main__" : 
    n = int(input())
    m = int(input())
    graph = [[sys.maxsize]*n for _ in range(n)]
    for _ in range(m) : 
        a, b, c = map(int, input().split())
        if graph[a-1][b-1] > c : 
            graph[a-1][b-1] = c

    graph = FW_joyGo(graph)
    for i in range(n) : 
        for j in range(n) : 
            if (graph[i][j] == sys.maxsize) or (i == j): 
                graph[i][j] = 0
    
    for line in graph : 
        print(*line)