# 백준25306 : 연속 XOR
def joyGo(n) : 
    res = 0
    for i in range(n//4 * 4, n+1) : 
        res ^= i
    return res

if __name__ == "__main__" : 
    A, B = map(int, input().split())
    print(joyGo(A-1) ^ joyGo(B))