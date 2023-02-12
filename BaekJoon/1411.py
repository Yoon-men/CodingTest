# 백준1411 : 비슷한 단어
import sys; input = sys.stdin.readline

def joyGo(N, Li) : 
    DiLi = [{} for _ in range(N)]
    checkLi = [[] for _ in range(N)]
    for i in range(N) : 
        word = Li[i]
        checkNum = 0
        for alphabet in word : 
            if alphabet not in DiLi[i] : 
                DiLi[i][alphabet] = checkNum
                checkNum += 1
            checkLi[i] += str(DiLi[i][alphabet])

    ans = 0
    for i in range(N) : 
        for j in range(i+1, N) : 
            if checkLi[i] == checkLi[j] : ans += 1
    
    return ans


if __name__ == "__main__" : 
    N = int(input())
    Li = [input().strip() for _ in range(N)]
    print(joyGo(N, Li))