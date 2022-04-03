# 별 찍기 - 2

starLine = int(input())
for gotcha in range(1, starLine + 1) : 
    blank = " " * (starLine - gotcha)
    star = "*" * gotcha
    print(f"{blank}{star}")