# 별 찍기 - 15
N = int(input())
print(f"{' ' * (N-1)}*")
for i in range(2, N+1) : 
    blank = " " * (N - i)
    blank_1 = " " * ((i-1)*2 - 1)
    star = "*"
    print(f"{blank}{star}{blank_1}{star}")