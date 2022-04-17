# 별 찍기 - 9
N = int(input())
for i in range(1, N + 1) : 
    blank = " " * (i - 1)
    star = "*" * (2*(N-i) + 1)
    print(f"{blank}{star}")
for i in range(1, N) : 
    blank = " " * (N-1 - i)
    star = "*" * (2*i + 1)
    print(f"{blank}{star}")