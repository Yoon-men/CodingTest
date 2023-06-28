# 백준2036 : 수열의 점수
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> int : 
    ans = 0
    plus_list, minus_list = [], []
    for i in Li : 
        if i > 1 : plus_list.append(i)
        elif i <= 0 : minus_list.append(i)
        else : ans += 1
    
    plus_list.sort(reverse=True)
    minus_list.sort()

    if len(plus_list) % 2 == 0 : 
        for i in range(0, len(plus_list), 2) : 
            ans += plus_list[i] * plus_list[i+1]
    else : 
        for i in range(0, len(plus_list)-1, 2) : 
            ans += plus_list[i] * plus_list[i+1]
        ans += plus_list[-1]

    if len(minus_list) % 2 == 0 : 
        for i in range(0, len(minus_list), 2) : 
            ans += minus_list[i] * minus_list[i+1]
    else : 
        for i in range(0, len(minus_list)-1, 2) : 
            ans += minus_list[i] * minus_list[i+1]
        ans += minus_list[-1]

    return ans


if __name__ == "__main__" : 
    Li = [int(input()) for _ in range(int(input()))]

    print(joyGo(Li))