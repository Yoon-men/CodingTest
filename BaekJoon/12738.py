# 백준12738 : 가장 긴 증가하는 부분 수열 3
def binaryJoyGo(s, e) : 
    while s <= e : 
        m = (s+e) // 2
        if ansLi[m] < Li[i] : s = m + 1
        else : e = m - 1

    return s


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))

    ansLi = [Li[0]]
    for i in range(N) : 
        if ansLi[-1] < Li[i] : ansLi.append(Li[i])
        else : ansLi[binaryJoyGo(0, len(ansLi)-1)] = Li[i]

    print(len(ansLi))