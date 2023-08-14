# 백준14912 : 숫자 빈도수
def joyGo(n: int, m: int) : 
    ans = 0
    for i in range(1, n+1) : 
        ans += str(i).count(str(m))

    return ans


if __name__ == "__main__" : 
    n, m = map(int, input().split())
    print(joyGo(n, m))