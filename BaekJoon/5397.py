# 백준5397 : 키로거
import sys ; input = sys.stdin.readline
for _ in range(int(input())) : 
    L, R = [], []
    for i in input().strip() : 
        if i=="-" : 
            if L : L.pop()
        elif i=="<" : 
            if L : R.append(L.pop())
        elif i==">" : 
            if R : L.append(R.pop())
        else : 
            L.append(i)
    print("".join(L) + "".join(reversed(R)))