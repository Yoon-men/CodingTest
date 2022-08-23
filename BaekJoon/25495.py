# 백준25495 : 에어팟
import sys
input = sys.stdin.readline
_ = int(input())
phones = list(map(int, input().split()))
joyGo = 0
temp = 0
answer = 0
for i in phones : 
    if i == joyGo : 
        temp *= 2
        answer += temp
    else : 
        joyGo = i
        temp = 2
        answer += 2
    if answer >= 100 : 
        answer = 0
        temp = 0
        joyGo = 0
print(answer)