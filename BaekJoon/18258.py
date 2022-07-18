# 백준18258 : 큐 2
from collections import deque
import sys
input = sys.stdin.readline
li = deque()

for _ in range(int(input())) : 
    cmd = input().split()
    if cmd[0] == "push" : 
        li.append(cmd[1])
    if cmd[0] == "pop" : 
        print(li.popleft() if len(li) != 0 else -1)
    if cmd[0] == "size" : 
        print(len(li))
    if cmd[0] == "empty" : 
        print(1 if len(li) == 0 else 0)
    if cmd[0] == "front" : 
        print(li[0] if len(li) != 0 else -1)
    if cmd[0] == "back" : 
        print(li[-1] if len(li) != 0 else -1)