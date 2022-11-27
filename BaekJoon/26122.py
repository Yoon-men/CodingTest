# 백준26122 : 가장 긴 막대 자석
def joyGo(s) : 
    current = s[0]
    recentCnt = 0 ; currentCnt = 0
    res = 0
    for i in s : 
        if i == current : currentCnt += 1
        else : 
            current = i
            res = max(res, min(currentCnt, recentCnt))
            recentCnt = currentCnt
            currentCnt = 1
    
    res = max(res, min(currentCnt, recentCnt))
    return res * 2

if __name__ == "__main__" : 
    _ = int(input())
    string = input()

    print(joyGo(string))