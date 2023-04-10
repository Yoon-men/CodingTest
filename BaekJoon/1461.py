# 백준1461 : 도서관
import sys; input = sys.stdin.readline

def solve(N: int, M: int, Li: list) -> int : 
    left, right = [], []
    for distance in Li : 
        if distance > 0 : right.append(distance)
        else : left.append(-distance)
    left.sort(reverse=True)
    right.sort(reverse=True)

    distance_list = []
    for idx in range(len(left)//M) : 
        distance_list.append(left[M*idx])
    if len(left)%M > 0 : 
        distance_list.append(left[len(left)//M*M])
    for idx in range(len(right)//M) : 
        distance_list.append(right[M*idx])
    if len(right)%M > 0 : 
        distance_list.append(right[len(right)//M*M])

    distance_list.sort(reverse=True)
    ans = 0
    ans += distance_list[0]
    ans += 2*sum(distance_list[1:])

    return ans


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = list(map(int, input().split()))
    print(solve(N, M, Li))