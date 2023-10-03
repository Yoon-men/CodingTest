# 백준8979 : 올림픽
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, K: int, infos: List[int]) -> int : 
    infos.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    k_idx = [team[0] for team in infos].index(K)
    for i in range(N) : 
        if infos[k_idx][1:] == infos[i][1:] : return i+1


if __name__ == "__main__" : 
    N, K = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(N)]
    print(joyGo(N, K, infos))