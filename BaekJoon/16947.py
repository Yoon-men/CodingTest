# 백준16947 : 서울 지하철 2호선
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from collections import deque

def joyGo(N: int, graph: list) -> list : 
    # DFS: Check if there is a cycle starting from the start_node.
    def DFS(start_node: int, cnt: int) -> int : 
        if visited[start_node] : 
            if cnt - dist[start_node] >= 3 : 
                return start_node
            else : 
                return -1

        visited[start_node] = 1
        dist[start_node] = cnt

        for next_node in graph[start_node] : 
            start_node_of_cycle = DFS(next_node, cnt+1)
            if start_node_of_cycle != -1 : 
                visited[start_node] = 2
                if start_node == start_node_of_cycle : return -1
                else : return start_node_of_cycle

        return -1

    # BFS: Check how far away each node is from the cycle.
    def BFS() -> list : 
        ans_list = [-1] * N
        dq = deque()

        for node in range(N) : 
            if visited[node] == 2 : 
                ans_list[node] = 0
                dq.append(node)

        while dq : 
            cur_node = dq.popleft()
            for next_node in graph[cur_node] : 
                if ans_list[next_node] == -1 : 
                    ans_list[next_node] = ans_list[cur_node] + 1
                    dq.append(next_node)
        
        return ans_list


    visited = [0] * N
    dist = [0] * N

    DFS(0, 0)
    ans_list = BFS()

    return ans_list



if __name__ == "__main__" : 
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N) : 
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    print(*joyGo(N, graph))