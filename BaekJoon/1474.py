# 백준1474 : 밑줄
import sys ; input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]

lineShare, lineRemainder = divmod(M-sum(map(len, words)), N-1)      # output : (몫), (나머지)
ans = words[0]
for i in range(1, N) : 
    if (words[i][0].islower()) and (lineRemainder != 0) : 
        ans += "_"*(lineShare+1) + words[i]
        lineRemainder -= 1
    elif i + lineRemainder == N : 
        ans += "_"*(lineShare+1) + words[i]
        lineRemainder -= 1
    else : 
        ans += "_"*lineShare + words[i]

print(ans)