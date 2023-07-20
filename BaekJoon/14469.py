# 백준14469 : 소가 길을 건너간 이유 3
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> int : 
    Li.sort()
    ans = 0
    for arrival_time, required_time in Li : 
        if ans > arrival_time : 
            ans += required_time
        else : 
            ans = arrival_time + required_time
    
    return ans


if __name__ == "__main__" : 
    Li = [list(map(int, input().split())) for _ in range(int(input()))]
    print(joyGo(Li))