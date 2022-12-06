# 백준6550 : 부분 문자열
import sys ; input = sys.stdin.readline

def chk(s, t) : 
    idx = 0
    for i in range(len(t)) : 
        if t[i] == s[idx] : 
            idx += 1
            if idx == len(s) : return "Yes"
    return "No"

if __name__ == "__main__" : 
    while True : 
        try : 
            s, t = input().split()
            print(chk(s, t))
        except : 
            break