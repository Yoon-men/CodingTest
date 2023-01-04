# 백준2748 : 피보나치 수 2
def joyGo(n) : 
    fLi = [0, 1]
    for i in range(2, n+1) : 
        fLi.append(fLi[i-2] + fLi[i-1])
    return fLi[n]


if __name__ == "__main__" : 
    n = int(input())
    print(joyGo(n))