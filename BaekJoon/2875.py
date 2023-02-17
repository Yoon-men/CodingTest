# 백준2875 : 대회 or 인턴
N, M, K = map(int, input().split())
ans = 0
while (N >= 2) and (M >= 1) and (N+M >= K+3) : 
    N -= 2; M -= 1; ans += 1
print(ans)