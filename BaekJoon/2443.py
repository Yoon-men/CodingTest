# 별 찍기 - 6
N = int(input())
for i in range(N) : 
    blank = " " * i
    star = "*" * (2*N - ((i+1)*2 - 1))
    print(f"{blank}{star}")