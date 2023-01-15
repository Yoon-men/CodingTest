# 백준27160 : 할리갈리
import sys; input = sys.stdin.readline
from collections import defaultdict

def bell() : 
    for i in Di.items() : 
        if i[1] == 5 : 
            return "YES"
            
    return "NO"


if __name__ == "__main__" : 
    Di = defaultdict(int)
    for _ in range(int(input())) : 
        S, X = input().split(); X = int(X)
        Di[S] += X

    print(bell())