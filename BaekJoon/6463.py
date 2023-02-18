# 백준6463 : 팩트
import sys; input = sys.stdin.readline
from math import factorial

while True : 
    try : 
        N = int(input())
        for i in str(factorial(N))[::-1] : 
            if i != "0" : 
                print(f"{N:>5} -> {i}")
                break
    except : 
        break