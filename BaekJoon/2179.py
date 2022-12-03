# 백준2179 : 비슷한 단어
import sys ; input = sys.stdin.readline

def lenChk(a, b) : 
    res = 0
    for i in range(min(len(a), len(b))) : 
        if a[i] == b[i] : res += 1
        else : break
    return res

if __name__ == "__main__" : 
    N = int(input())
    Li = [input().strip() for _ in range(N)]
    sortedLi = sorted(list(enumerate(Li)), key=lambda x : x[1])

    lenChkLi = [0] * (N+1)
    maxLen = 0

    for i in range(N-1) : 
        iLen = lenChk(sortedLi[i][1], sortedLi[i+1][1])
        maxLen = max(maxLen, iLen)

        lenChkLi[sortedLi[i][0]] = max(lenChkLi[sortedLi[i][0]], iLen)
        lenChkLi[sortedLi[i+1][0]] = max(lenChkLi[sortedLi[i+1][0]], iLen)

    firstIsAppeared = 0
    for i in range(N) : 
        if not firstIsAppeared : 
            if lenChkLi[i] == maxLen : 
                firstIsAppeared = 1
                print(Li[i])
                pre = Li[i][:maxLen]
        else : 
            if lenChkLi[i] == maxLen and Li[i][:maxLen] == pre : 
                print(Li[i])
                break