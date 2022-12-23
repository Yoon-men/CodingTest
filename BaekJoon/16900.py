# 백준16900 : 이름 정하기
def piAryMaker(s) : 
    piAry = [0] * len(s)
    i = 0
    for j in range(1, len(s)) : 
        while (i > 0) and (s[i] != s[j]) : 
            i = piAry[i-1]
        
        if s[i] == s[j] : 
            i += 1
            piAry[j] = i
    
    return piAry


if __name__ == "__main__" : 
    S, K = input().split(); K = int(K)
    piAry = piAryMaker(S)

    len_S = len(S)
    print(len_S + (len_S - piAry[-1])*(K-1))