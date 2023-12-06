# 백준15988 : 1, 2, 3 더하기 3
import sys; input = sys.stdin.readline

Li = [1, 2, 4]
for _ in range(1000001): 
    Li.append(Li[-3]%1000000009 + Li[-2]%1000000009 + Li[-1]%1000000009)

for _ in range(int(input())): 
    print(Li[int(input())-1] % 1000000009)