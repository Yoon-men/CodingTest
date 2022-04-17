# 별 찍기 - 17
N = int(input())
for i in range(1, N + 1) : 
    if i == 1 or i == N : 
        blank = " " * (N - i)
        star = "*" * (i*2 - 1)
        print(f"{blank}{star}")
    else : 
        blank = " " * (N - i)
        blank_1 = " " * ((i-1)*2 - 1)
        star = "*"
        print(f"{blank}{star}{blank_1}{star}")