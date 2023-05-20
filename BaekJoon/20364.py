# 백준20364 : 부동산 다툼
import sys; input = sys.stdin.readline

def joyGo(N: int, Q: int, Li: list) -> list : 
    graph = [0] * (N+1)
    ans_list = []
    for x in Li : 
        fuck = 0
        tmp = x
        while tmp != 1 : 
            if graph[tmp] : 
                fuck = 1
                asshole = tmp
            tmp //= 2
        if fuck : 
            ans_list.append(asshole)
        else : 
            ans_list.append(0)
            graph[x] = 1

    return ans_list


if __name__ == "__main__" : 
    N, Q = map(int, input().split())
    Li = [int(input()) for _ in range(Q)]
    print("\n".join(map(str, joyGo(N, Q, Li))))