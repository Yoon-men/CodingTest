# 백준10813 : 공 바꾸기
N, M = map(int, input().split())
Li = list(range(1, N+1))
for _ in range(M) : 
    i, j = map(int, input().split())
    i -= 1; j -= 1
    Li[i], Li[j] = Li[j], Li[i]
print(*Li)