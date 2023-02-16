# 백준2693 : N번째 큰 수
import sys; input = sys.stdin.readline
for _ in range(int(input())) : 
    Li = sorted(list(map(int, input().split())), reverse=True)
    print(Li[2])