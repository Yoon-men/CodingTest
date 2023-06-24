# 백준4344 : 평균은 넘겠지
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list) -> float : 
    average = sum(Li) / N
    cnt = 0
    for s in Li : 
        if s > average : cnt += 1

    def fuckfuckfuckfuckfuckfuckfuckfuck(n: float, asshole: int) : 
        shit = 10**asshole
        n *= shit
        res = int(n)+1 if (n-int(n) >= 0.5) else int(n)
        return res / shit
    return f"{fuckfuckfuckfuckfuckfuckfuckfuck(cnt/N * 100, 3):.3f}"


if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        N, *Li = map(int, input().split())
        print(f"{joyGo(N, Li)}%")