# 통계학
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
bullShit = []

for _ in range(N) : 
    num = int(input())
    bullShit.append(num)


# < 산술평균 >
arithmeticMean = sum(bullShit) / N


# < 중앙값 >
bullShit.sort()
median = bullShit[N // 2]


# < 최빈값 >
## Example >> bullShit = [1, 1, 2, 2, 3]
if len(bullShit) == 1 : 
    mode = bullShit[0]
else : 
    holyShit = Counter(bullShit).most_common(2)
    ## Example >> holyShit = [(1, 2), (2, 2)]
    if holyShit[0][1] == holyShit[1][1] : 
        mode = holyShit[1][0]
        ## Example >> mode = 2
    else : 
        mode = holyShit[0][0]


# < 범위 >
range = bullShit[-1] - bullShit[0]


print(round(arithmeticMean))
print(median)
print(mode)
print(range)