# 백준2960 : 에라토스테네스의 체
N, K = map(int, input().split())
visited = [0] * (N+1)
cnt = 0
for i in range(2, N+1) : 
    if not visited[i] : 
        for j in range(i, N+1, i) : 
            if not visited[j] : 
                visited[j] = 1
                cnt += 1
                if cnt == K : 
                    print(j)
                    break