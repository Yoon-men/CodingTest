# 백준10811 : 바구니 뒤집기
N, M = map(int, input().split())
Li = list(range(1, N+1))
for _ in range(M) : 
    i, j = map(int, input().split()); i-=1; j-=1
    tmp = Li[i:j+1][::-1]
    for k in range(i, j+1) : 
        Li[k] = tmp[k-i]
print(*Li)