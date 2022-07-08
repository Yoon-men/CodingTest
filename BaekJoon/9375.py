# 백준9375 : 패션왕 신해빈
import sys
input = sys.stdin.readline


for _ in range(int(input())) : 
    answer = 1
    items = {}
    for __ in range(int(input())) : 
        name, kind = map(str, input().split())
        if kind not in items : 
            items[kind] = []     
        items[kind].append(name)

    for i in items.values() : 
        answer *= len(i)+1

    print(answer-1)