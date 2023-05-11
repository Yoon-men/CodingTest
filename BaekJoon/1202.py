# 백준1202 : 보석 도둑
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def joyGo(N: int, K: int, gem_list: list, bag_list: list) -> int : 
    gem_list.sort()
    bag_list.sort()

    queue = []
    ans = 0
    for bag in bag_list : 
        while (gem_list) and (gem_list[0][0] <= bag) : 
            heappush(queue, -gem_list[0][1])
            heappop(gem_list)
        ans += -heappop(queue) if queue else 0
    
    return ans


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    gem_list = [tuple(map(int, input().split())) for _ in range(N)]
    bag_list = [int(input()) for _ in range(K)]
    print(joyGo(N, K, gem_list, bag_list))