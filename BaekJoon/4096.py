# 백준4096 : 팰린드로미터
import sys ; input = sys.stdin.readline

def joyGo(s) : 
    ans = 0
    while True : 
        if s == s[::-1] : return ans
        s = str(int(s)+1).zfill(len(s))
        ans += 1

if __name__ == "__main__" : 
    while True : 
        s = input().strip()
        if s == "0" : break
        print(joyGo(s))