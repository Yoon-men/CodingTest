# 별 찍기 - 12
N = int(input())
for i in range(1, N + 1) : 
    star = "*" * i
    print(star)
for i in range(1, N) : 
    star = "*" * (N - i)
    print(star)