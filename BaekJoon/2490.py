# 윷놀이
for _ in range(3) : 
    RoLlInGtHuNdEr = list(map(int, input().split()))
    if RoLlInGtHuNdEr.count(0) == 1 : 
        print("A")
    elif RoLlInGtHuNdEr.count(0) == 2 : 
        print("B")
    elif RoLlInGtHuNdEr.count(0) == 3 : 
        print("C")
    elif RoLlInGtHuNdEr.count(0) == 4 : 
        print("D")
    else : 
        print("E")