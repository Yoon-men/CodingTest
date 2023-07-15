# 백준5567 : 결혼식
import sys; input = sys.stdin.readline

def joyGo(n: int, graph: list) -> int : 
    def DFS(friend: int, depth: int) : 
        visited[friend] = 1
        if depth == 2 : return
        for f_friend in graph[friend] : 
            if not visited[f_friend] : 
                visited[f_friend] = 1
            DFS(f_friend, depth+1)


    visited = [0] * n
    DFS(friend=0, depth=0)

    return sum(visited) - 1



if __name__ == "__main__" : 
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(int(input())) : 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    print(joyGo(n, graph))