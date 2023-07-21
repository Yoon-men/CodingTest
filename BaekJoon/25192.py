# 백준25192 : 인사성 밝은 곰곰이
import sys; input = sys.stdin.readline

def joyGo(Li: list) : 
    ans = 0
    Se = set()
    for i in Li : 
        if i == "ENTER" : 
            Se.clear()
            continue

        if i not in Se : 
            Se.add(i)
            ans += 1

    return ans


if __name__ == "__main__" : 
    Li = [input().strip() for _ in range(int(input()))]
    print(joyGo(Li))