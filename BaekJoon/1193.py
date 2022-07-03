# 백준1193 : 분수 찾기
import sys
X = int(sys.stdin.readline())
line, sequence = 0, 0

while X > sequence : 
    line += 1
    sequence += line

if line % 2 == 0 : 
    a = line - sequence + X
    b = sequence - X + 1
else : 
    a = sequence - X + 1
    b = line - sequence + X

print(f"{a}/{b}")