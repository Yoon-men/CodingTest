# 백준1312 : 소수
A, B, N = map(int, input().split())
for _ in range(N) : 
    A = A%B * 10
    answer = A//B
print(answer)