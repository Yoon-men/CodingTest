# 백준1138 : 한 줄로 서기
N = int(input())
Li = list(map(int, input().split()))
ans = [0]*N

for i in range(N) : 
    cnt = 0
    for j in range(N) : 
        if (cnt == Li[i]) and (ans[j] == 0) : 
            ans[j] = i+1
            break
        elif ans[j] == 0 : 
            cnt += 1

print(*ans)