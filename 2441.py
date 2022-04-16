# 별 찍기 - 4
N = int(input())
for i in range(N) : 
    blank = " " * i
    star = "*" * (N - i)
    print(f"{blank}{star}")