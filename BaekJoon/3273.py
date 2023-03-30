 # 백준3273: 두 수의 합
def joyGo(Li: list, x: int) -> int : 
    ans = 0
    s, e = 0, len(Li)-1
    while s < e : 
        summ = Li[s] + Li[e]
        if summ == x : 
            ans += 1
            s += 1
        elif summ < x : 
            s += 1
        else : 
            e -= 1
    
    return ans

if __name__ == "__main__" : 
    n = int(input())
    Li = sorted(list(map(int, input().split())))
    x = int(input())

    print(joyGo(Li, x))