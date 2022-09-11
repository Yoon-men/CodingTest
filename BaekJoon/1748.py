# 백준1748 : 수 이어 쓰기 1
N = int(input())
L = len(str(N))
cnt = 0
for i in range(L-1) : 
    cnt += 9 * 10**i * (i+1)
print(cnt + (N - 10**(L-1) + 1)*L)