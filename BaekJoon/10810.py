# 백준10810 : 공 넣기
N, M = map(int, input().split())
basket = [0] * N
for _ in range(M) : 
    i, j, k = map(int, input().split())
    for num in range(i, j+1) : 
        basket[num-1] = k
print(*basket)