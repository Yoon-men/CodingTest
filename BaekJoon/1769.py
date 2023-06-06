# 백준1769 : 3의 배수
def joyGo(X: str) -> list : 
    cnt = 0
    while (len(X) != 1) : 
        tmp = 0
        for i in X : 
            tmp += int(i)
        X = str(tmp)
        cnt += 1

    ans = "YES" if int(X) % 3 == 0 else "NO"

    return [cnt, ans]


if __name__ == "__main__" : 
    X = input()
    print("\n".join(map(str, joyGo(X))))