# 백준25904 : 안녕 클레오파트라 세상에서 제일가는 포테이토칩
def joyGo() : 
    s = X
    while True : 
        for i in range(N) : 
            if Li[i] < s : return i+1
            s += 1

if __name__ == "__main__" : 
    N, X = map(int, input().split())
    Li = list(map(int, input().split()))
    print(joyGo())