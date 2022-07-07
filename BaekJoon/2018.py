# 백준2018 : 수들의 합 5
import sys
N = int(sys.stdin.readline())

start, end = 1, 2
joyGo = start + end
count = 0
while start <= N//2 : 
    if joyGo < N : 
        end += 1
        joyGo += end
    elif joyGo == N : 
        end += 1
        joyGo += end
        joyGo -= start
        start += 1
        count += 1
    else : 
        joyGo -= start
        start += 1

print(count+1)