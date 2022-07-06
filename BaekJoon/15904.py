# 백준15904 : UCPC는 무엇의 약자일까?
import sys

def check(t) : 
    UCPC = list("UCPC")
    for i in t : 
        if "U" in i or "C" in i or "P" in i : 
            i = list(i)
            for j in i : 
                if j[0] == UCPC[0] : 
                    UCPC.pop(0)
                if len(UCPC) == 0 : 
                    return "I love UCPC"
    return "I hate UCPC"

if __name__ == "__main__" : 
    text = list(map(str, sys.stdin.readline().split()))
    print(check(text))