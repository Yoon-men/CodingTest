# 백준5613 : 계산기 프로그램
import sys; input = sys.stdin.readline

ans = int(input())
while True: 
    op = input().strip()
    if op == '=': break

    n = int(input())
    if op == '+': ans += n
    elif op == '-': ans -= n
    elif op == '*': ans *= n
    elif op == '/': ans //= n

print(ans)