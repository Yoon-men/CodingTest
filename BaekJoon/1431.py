# 백준1431 : 시리얼 번호
import sys ; input = sys.stdin.readline
def joyGo(s) : 
    res = 0
    for i in s : 
        if i.isdigit() : res += int(i)
    return res
if __name__ == "__main__" : 
    Li = [input().strip() for _ in range(int(input()))]
    for i in sorted(Li, key=lambda x : (len(x), joyGo(x), x)) : 
        print(i)