# 백준29791 : 에르다 노바와 오리진 스킬
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(N: int, M: int, erda_list: List[int], origin_list: List[int]) -> Tuple[int, int] : 
    erda, origin = 1, 1
    erda_list.sort()
    origin_list.sort()

    skill_time = erda_list[0]
    for i in range(1, N) : 
        if skill_time + 100 <= erda_list[i] : 
            erda += 1
            skill_time = erda_list[i]

    skill_time = origin_list[0]
    for i in range(1, M) : 
        if skill_time + 360 <= origin_list[i] : 
            origin += 1
            skill_time = origin_list[i]

    return (erda, origin)


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    erda_list = list(map(int, input().split()))
    origin_list = list(map(int, input().split()))
    print(*joyGo(N, M, erda_list, origin_list))