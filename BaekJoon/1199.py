# 백준1199 : 오일러 회로
import sys; input = sys.stdin.readline

def isEulerianCircuit() : 
    for i in degreeLi : 
        if i%2 == 1 : return False
    return True

def joyGo(cur) : 
    global graph, visited
    ansLi = []
    stack = [cur]
    while stack : 
        cur = stack[-1]
        if graph[cur] : 
            target = next(iter(graph[cur]))
            visited[cur][target] -= 1
            visited[target][cur] -= 1
            
            if not visited[cur][target] : 
                del graph[cur][target]
                del graph[target][cur]
            stack.append(target)
        
        else : 
            ansLi.append(stack.pop()+1)

    return ansLi


if __name__ == "__main__" : 
    N = int(input())
    adjacentMatrix = [list(map(int, input().split())) for _ in range(N)]
    graph = [[] for _ in range(N)]
    degreeLi = [0] * N
    visited = [[0]*N for _ in range(N)]
    for i in range(N) : 
        tmpDi = {}
        for u, v in enumerate(adjacentMatrix[i]) : 
            if v > 0 : 
                degreeLi[i] += v
                visited[i][u] = v
                tmpDi[u] = 1
        graph[i] = tmpDi

    if not isEulerianCircuit() : print(-1)
    else : print(" ".join(str(i) for i in joyGo(0)))