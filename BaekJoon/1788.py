# 백준1788 : 피보나치 수의 확장
def joyGo(N) : 
    if N > 0 : flag = 1
    elif N == 0 : flag = 0
    else : flag = -1 if abs(N)%2 == 0 else 1

    fLi = [0, 1]
    for i in range(2, abs(N)+1) : 
        fLi.append((fLi[i-2]+fLi[i-1]) % 10**9)

    return (flag, fLi[abs(N)])

if __name__ == "__main__" : 
    print("\n".join(map(str, joyGo(int(input())))))