# 백준17299 : 오등큰수
from collections import Counter

def NGF(n) : 
    for i in A[n+1:] :         
        if cnt[A[n]] < cnt[i] : 
            return i

    return -1

if __name__ == "__main__" : 
    N = int(input())
    A = list(map(int, input().split()))
    
    cnt = Counter(A)
    
    answer = [NGF(i) for i in range(N)]
    print(*answer)