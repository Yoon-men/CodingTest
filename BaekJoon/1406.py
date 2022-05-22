# 에디터
import sys
input = sys.stdin.readline
sentence = list(input().strip())        # 입력 이후 LOC로 전락.
ROC = []                                # ROC, Right Of the Cursor.
LOC = sentence                          # LOC, Left Of the Cursor.
M = int(input())
for i in range(M) : 
    command = list(map(str, input().split()))
    if command[0] == "L" and len(LOC) != 0 : 
        ROC.append(LOC.pop())
    if command[0] == "D" and len(ROC) != 0 : 
        LOC.append(ROC.pop())
    if command[0] == "B" and len(LOC) != 0 : 
        LOC.pop()
    if command[0] == "P" : 
        LOC.append(command[1])
print("".join(LOC + list(reversed(ROC))))