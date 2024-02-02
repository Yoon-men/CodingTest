# 백준1719 : 택배
import sys; input = sys.stdin.readline
from typing import List, Union, Tuple

def joyGo(n: int, m: int, road_info: List[Tuple[int, int, int]]) -> List[List[Union[int, str]]]: 
    ans = [['-' for _ in range(n+1)] for _ in range(n+1)]

    graph = [[sys.maxsize] * (n+1) for _ in range(n+1)]
    for u, v, w in road_info: 
        graph[u][v] = w
        graph[v][u] = w

        ans[u][v] = v
        ans[v][u] = u

    for k in range(1, n+1): 
        for i in range(1, n+1): 
            for j in range(1, n+1): 
                if (i != j) and (graph[i][j] > graph[i][k] + graph[k][j]): 
                    graph[i][j] = graph[i][k] + graph[k][j]
                    ans[i][j] = ans[i][k]

    ans = [row[1:] for row in ans[1:]]

    return ans


if __name__ == "__main__": 
    n, m = map(int, input().split())
    road_info = [tuple(map(int, input().split())) for _ in range(m)]
    
    ans = joyGo(n, m, road_info)
    for row in ans: 
        print(*row)



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, n, m, road_info, ans"), 
    [
        (
            1, 
            6, 10, 
            [(1, 2, 2), (1, 3, 1), (2, 4, 5), (2, 5, 3), (2, 6, 7), (3, 4, 4), (3, 5, 6), (3, 6, 7), (4, 6, 4), (5, 6, 2)], 
            [['-', 2, 3, 3, 2, 2], [1, '-', 1, 4, 5, 5], [1, 1, '-', 4, 5, 6], [3, 2, 3, '-', 6, 6], [2, 2, 3, 6, '-', 6], [5, 5, 3, 4, 5, '-']]
        )
    ]
)

def test_joyGo(case_num: int, n: int, m: int, road_info: List[Tuple[int, int, int]], ans: List[List[Union[int, str]]]) -> None: 
    res = joyGo(n, m, road_info)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ