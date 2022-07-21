# 백준5430 : AC
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())) : 
    cmd = input()
    n = int(input())
    arr = deque(input()[1:-2].split(","))

    if n == 0 : 
        arr = deque()

    checkReverse = 0
    for i in cmd : 
        if i == "R" : 
            checkReverse += 1
        
        elif i == "D" : 
            if len(arr) == 0 : 
                print("error")
                break
            else : 
                if checkReverse % 2 == 0 : 
                    arr.popleft()
                else : 
                    arr.pop()

    else : 
        if checkReverse % 2 == 0 : 
            print(f"[{','.join(arr)}]")
        else : 
            arr.reverse()
            print(f"[{','.join(arr)}]")