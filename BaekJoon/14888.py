# 백준14888 : 연산자 끼워넣기
import sys; input = sys.stdin.readline
from typing import List, Tuple

def joyGo(N: int, num_list: List[int], op_list: List[int]) -> Tuple[int, int]: 
    def DFS(dep: int, num: int, add: int, sub: int, mul: int, div: int) -> None: 
        if dep == N: 
            possible_list.append(num)
            return
        
        if add: DFS(dep+1, num+num_list[dep], add-1, sub, mul, div)
        if sub: DFS(dep+1, num-num_list[dep], add, sub-1, mul, div)
        if mul: DFS(dep+1, num*num_list[dep], add, sub, mul-1, div)
        if div: DFS(dep+1, int(num/num_list[dep]), add, sub, mul, div-1)

        return

    
    possible_list = []
    DFS(dep=1, num=num_list[0], add=op_list[0], sub=op_list[1], mul=op_list[2], div=op_list[3])

    possible_list.sort()
    return (possible_list[-1], possible_list[0])



if __name__ == "__main__": 
    N = int(input())
    num_list = list(map(int, input().split()))
    op_list = list(map(int, input().split()))

    print(*joyGo(N, num_list, op_list), sep='\n')



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, num_list, op_list, ans"),
    [
        (1, 2, [5, 6], [0, 0, 1, 0], (30, 30)),
        (2, 3, [3,4,5], [1,0,1,0], (35,17)),
        (3, 6, [1,2,3,4,5,6], [2,1,1,1], (54, -24))
    ]
)

def test_joyGo(case_num: int, N: int, num_list: List[int], op_list: List[int], ans: Tuple[int, int]) -> None:
    res = joyGo(N, num_list, op_list) 
    assert res == ans, f"Test Case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ