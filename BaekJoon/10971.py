# 백준10971 : 외판원 순회 2
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, matrix: List[List[int]]) -> int: 
    def dfs(start: int, current: int, visited: List[bool], cost: int) -> None: 
        nonlocal ans

        if all(visited): 
            if matrix[current][start]: ans = min(ans, cost + matrix[current][start])
            return
        
        for next in range(N): 
            if (visited[next]) or (matrix[current][next] == 0): continue

            visited[next] = True
            dfs(start, next, visited, cost + matrix[current][next])
            visited[next] = False
        
        return


    ans = sys.maxsize
    for start in range(N): 
        visited = [False] * N
        visited[start] = True
        dfs(start, start, visited, 0)
        visited[start] = False
    
    return ans



if __name__ == "__main__": 
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(joyGo(N, matrix))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("N, matrix, ans"), 
    [
        (4, [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]], 35)
    ]
)

def test_joyGo(N: int, matrix: List[List[int]], ans: int) -> None: 
    res = joyGo(N, matrix)
    assert res == ans, f"Test case - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ