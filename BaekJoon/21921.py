# 백준21921 : 블로그
import sys; input = sys.stdin.readline

def joyGo(N: int, X: int, Li: list) -> str : 
    if sum(Li) == 0 : return "SAD"

    sum_checker = ans = sum(Li[:X])
    cnt = 1
    for i in range(1, N-X+1) : 
        sum_checker = sum_checker - Li[i-1] + Li[i+X-1]
        if sum_checker > ans : 
            ans = sum_checker
            cnt = 1
        elif sum_checker == ans : 
            cnt += 1
    
    return f"{ans}\n{cnt}"
    

if __name__ == "__main__" : 
    N, X = map(int, input().split())
    Li = list(map(int, input().split()))

    print(joyGo(N, X, Li))