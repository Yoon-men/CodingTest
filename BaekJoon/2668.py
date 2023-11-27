# 백준2668 : 숫자고르기
import sys; input = sys.stdin.readline
from typing import List, Tuple
sys.setrecursionlimit(10**9)

def joyGo(N: int, num_list: List[int]) -> Tuple[int, List[int]]: 
    def DFS(n: int) -> None: 
        visited[n] = 1
        cycle_list.append(n)

        next_num = num_list[n]
        if visited[next_num] == 1: 
            if next_num in cycle_list: 
                nonlocal ans_list
                ans_list += cycle_list[cycle_list.index(next_num):]
            return

        DFS(next_num)

    ans_list = []
    num_list = [0] + num_list
    visited = [-1] * (N+1)

    for i in range(1, N+1): 
        if visited[i] == -1: 
            cycle_list = []
            DFS(i)
    
    return (len(ans_list), sorted(ans_list))


if __name__ == "__main__": 
    N = int(input())
    num_list = [int(input()) for _ in range(N)]

    len_Li, Li = joyGo(N, num_list)
    print(len_Li)
    print(*Li, sep='\n')



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this line. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("N, num_list, ans"), 
    [
        (7, [3,1,1,5,5,4,6], (3, [1, 3, 5]))
    ]
)

def test_joyGo(N: int, num_list: List[int], ans: Tuple[int, List[int]]) -> None: 
    res = joyGo(N, num_list)
    assert res == ans, f"Test case - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this line. > ㅛㅛㅛㅛㅛㅛ