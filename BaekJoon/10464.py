# 백준10464 : XOR
import sys; input = sys.stdin.readline

def joyGo(n) : 
    res = 0
    for i in range(n//4 * 4, n+1) : 
        res ^= i
    return res

if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        S, F = map(int, input().split())
        print(joyGo(S-1) ^ joyGo(F))