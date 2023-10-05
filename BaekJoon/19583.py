# 백준19583 : 싸이버개강총회
import sys; input = sys.stdin.readline
from datetime import datetime

S, E, Q = input().split()
S, E, Q = datetime.strptime(S, "%H:%M"), datetime.strptime(E, "%H:%M"), datetime.strptime(Q, "%H:%M")
hello, bye = set(), set()
while True : 
    try : 
        time, man = input().split()
        time = datetime.strptime(time, "%H:%M")
        if time <= S : 
            hello.add(man)
        elif E <= time <= Q : 
            bye.add(man)
    except : 
        break
print(len(hello & bye))