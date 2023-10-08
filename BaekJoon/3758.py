# 백준3758 : KCPC
import sys; input = sys.stdin.readline
from typing import List

def joyGo(n: int, k: int, t: int, log: List[List[int]]) : 
    # n = (팀의 개수); k = (문제의 개수); t = (당신 팀의 ID); m = (로그 엔트리의 개수)
    # i = (팀 ID); j = (문제 번호); s = (획득한 점수)
    Di = {i: {"score_list": [0] * k, "submit_cnt": 0, "submit_time": 0} for i in range(1, n+1)}
    for submit_time, data in enumerate(log) : 
        i, j, s = data
        Di[i]["score_list"][j-1] = max(s, Di[i]["score_list"][j-1])
        Di[i]["submit_cnt"] += 1
        Di[i]["submit_time"] = submit_time

    sorted_Di = sorted(Di.items(), key=lambda x: (-sum(x[1]["score_list"]), x[1]["submit_cnt"], x[1]["submit_time"]))

    ranking_dict = {i: 0 for i in range(1, n+1)}
    for i in range(n) : ranking_dict[sorted_Di[i][0]] = i+1

    return ranking_dict[t]


if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        n, k, t, m = map(int, input().split())
        log = [list(map(int, input().split())) for _ in range(m)]
        print(joyGo(n, k, t, log))