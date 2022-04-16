# 별 찍기 - 12
N = int(input())
for i in range(1, N + 1) : 
    blank = " " * (N - i)
    star = "*" * i
    print(f"{blank}{star}")
for i in range(1, N) : 
    blank = " " * i
    star = "*" * (N - i)
    print(f"{blank}{star}")