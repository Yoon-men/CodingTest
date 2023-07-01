# 백준18110 : solved.ac
import sys; input = sys.stdin.readline

def joyGo(n: int, Li: list) -> int : 
    if n == 0 : return 0

    def round(N: float) : 
        return int(N)+1 if (N-int(N) >= 0.5) else int(N)
    
    cut = round(n*0.15)
    Li = sorted(Li)[cut:n-cut]

    return round(sum(Li)/len(Li))


if __name__ == "__main__" : 
    n = int(input())
    Li = [int(input()) for _ in range(n)]

    print(joyGo(n, Li))