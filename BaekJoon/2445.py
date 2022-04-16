# 별 찍기 - 8
N = int(input())
for i in range(1, N + 1) : 
    blank = " " * (N*2 - i*2)
    star = "*" * i
    print(f"{star}{blank}{star}")
for i in range(1, N) : 
    blank = " " * (N*2 - (N-i)*2)
    star = "*" * (N - i)
    print(f"{star}{blank}{star}")