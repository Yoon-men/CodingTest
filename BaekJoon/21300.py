# 백준21300 : Bottle Return
import sys
kinds = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in kinds : 
    answer += i*5
print(answer)