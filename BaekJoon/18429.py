# 백준18429 : 근손실
def DFS(cnt, weight) : 
    if cnt == N : 
        global ans
        ans += 1
    else : 
        for i in range(N) : 
            if (not visited[i]) and (weight+Li[i]-K >= 0) : 
                visited[i] = 1
                DFS(cnt+1, weight+Li[i]-K)
                visited[i] = 0

if __name__ == "__main__" : 
    N, K = map(int, input().split())
    Li = list(map(int, input().split()))
    
    visited = [0] * N
    ans = 0
    DFS(0, 0)

    print(ans)