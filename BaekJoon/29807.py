# 29807: 학번을 찾아줘!
import sys; input = sys.stdin.readline
from typing import List

def joyGo(T: int, score_list: List[int]) : 
    score_list.extend([0] * (5-T))

    ans = 0
    ans += abs(score_list[0]-score_list[2]) * (508 if score_list[0] > score_list[2] else 108)
    ans += abs(score_list[1]-score_list[3]) * (212 if score_list[1] > score_list[3] else 305)
    if score_list[4] : ans += score_list[4] * 707

    return ans * 4763


if __name__ == "__main__" : 
    T = int(input())
    score_list = list(map(int, input().split()))
    print(joyGo(T, score_list))