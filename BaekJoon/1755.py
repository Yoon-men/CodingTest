# 백준1755 : 숫자놀이
def joyGo(s, e) : 
    numDi = {str(i) : j for i, j in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])}
    Li = []

    for i in range(s, e+1) : 
        tmp = " ".join(numDi[j] for j in str(i))
        Li.append((tmp, i))

    return sorted(Li)


if __name__ == "__main__" : 
    M, N = map(int, input().split())

    ansLi = joyGo(M, N)
    for i in range(len(ansLi)) : 
        if (i % 10 == 0) and (i != 0) : print()
        print(ansLi[i][1], end=" ")