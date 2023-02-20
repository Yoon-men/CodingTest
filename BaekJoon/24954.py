# 백준24954 : 물약 구매
import sys; input = sys.stdin.readline
from itertools import permutations

def joyGo(N, Li, discountLi) : 
    permutationLi = list(permutations(range(N), N))
    ans = sys.maxsize
    for permutation in permutationLi : 
        tmpLi = Li[:]
        tmp = 0
        for item in permutation : 
            tmp += tmpLi[item]
            for target, price in discountLi[item] : 
                discounted = tmpLi[target-1] - price
                tmpLi[target-1] = discounted if discounted > 0 else 1
        ans = min(ans, tmp)
    
    return ans


if __name__ == "__main__" : 
    N = int(input())
    Li = list(map(int, input().split()))

    discountLi = [[] for _ in range(N)]
    for i in range(N) : 
        for _ in range(int(input())) : 
            discountLi[i].append(list(map(int, input().split())))
    
    print(joyGo(N, Li, discountLi))