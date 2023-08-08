# 백준28279 : 덱 2
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(cmd_list: list) -> None : 
    dq = deque()
    for cmd in cmd_list : 
        if cmd[0] == 1 : dq.appendleft(cmd[1])
        elif cmd[0] == 2 : dq.append(cmd[1])
        elif cmd[0] == 3 : print(dq.popleft() if dq else -1)
        elif cmd[0] == 4 : print(dq.pop() if dq else -1)
        elif cmd[0] == 5 : print(len(dq))
        elif cmd[0] == 6 : print(1 if not dq else 0)
        elif cmd[0] == 7 : print(dq[0] if dq else -1)
        elif cmd[0] == 8 : print(dq[-1] if dq else -1)

if __name__ == "__main__" : 
    cmd_list = [list(map(int, input().split())) for _ in range(int(input()))]
    joyGo(cmd_list)