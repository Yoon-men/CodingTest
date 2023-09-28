# 백준26607 : 시로코와 은행털기
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(n: int, k: int, x: int, mans: List[Tuple[int, int]]) : 
    strength_list = [man[0] for man in mans]
    
    dp = [[0]*(n*x+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n) : 
        for j in range(min(i+1, k), 0, -1) : 
            for a in range(j*x, strength_list[i]-1, -1) : 
                dp[j][a] = dp[j][a] or dp[j-1][a-strength_list[i]]
    
    ans = 0
    for i in range(k*x+1) : 
        if dp[k][i] : ans = max(ans, i * (k*x - i))
    
    return ans


if __name__ == "__main__" : 
    n, k, x = map(int, input().split())
    mans = [list(map(int, input().split())) for _ in range(n)]

    print(joyGo(n, k, x, mans))