# 백준25704 : 출석 이벤트
def joyGo(n, p) : 
    DC = [0]
    if n >= 5 : DC.append(500)
    if n >= 10 : DC.append(p // 10)
    if n >= 15 :DC.append(2000)
    if n >= 20 : DC.append(p // 4)
    ans = p - max(DC)
    if ans < 0 : ans = 0
    return ans

if __name__ == "__main__" : 
    N = int(input())
    P = int(input())
    print(joyGo(N, P))