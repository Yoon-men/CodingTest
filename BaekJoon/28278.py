# 백준28278: 스택 2
import sys; input = sys.stdin.readline

s = []
for _ in range(int(input())) : 
    cmd = input().split()
    if cmd[0] == '1' : s.append(cmd[1])
    elif cmd[0] == '2' : print(s.pop() if s else -1)
    elif cmd[0] == '3' : print(len(s))
    elif cmd[0] == '4' : print(0 if s else 1)
    elif cmd[0] == '5' : print(s[-1] if s else -1)