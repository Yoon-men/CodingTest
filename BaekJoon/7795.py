# 백준7795 : 먹을 것인가 먹힐 것인가
import sys; input = sys.stdin.readline
from typing import List

def joyGo(N: int, M: int, a_list: List[int], b_list: List[int]) -> int: 
    def getPreyNum(eater: int) -> int: 
        '''
        이분 탐색을 사용해 주어진 eater가 먹을 수 있는 먹이 개수를 구합니다.

        Parameters: 
            eater (int): 먹이를 먹으려는 eater의 크기
        
        Returns: 
            int: 주어진 eater가 먹을 수 있는 먹이 개수

        '''
        s, e = 0, len(b_list)-1
        while s <= e: 
            m = (s + e) // 2
            if b_list[m] < eater: 
                s = m + 1
            else: 
                e = m - 1
        
        return s
    
        ### ----- getPreyNum() end ----- ###


    a_list.sort()
    b_list.sort()

    ans = 0
    for a in a_list: 
        ans += getPreyNum(eater= a)
    
    return ans

    ### ----- joyGo() end ----- ###



if __name__ == "__main__": 
    for _ in range(int(input())): 
        N, M = map(int, input().split())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))

        print(joyGo(N, M, a_list, b_list))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, M, a_list, b_list, ans"), 
    [
        (
            1, 
            5, 3, 
            [8, 1, 7, 3, 1], [3, 6, 1], 
            7
        ), 
        (
            2, 
            3, 4, 
            [2, 13, 7], [103, 11, 290, 215], 
            1
        )
    ]
)

def test_joyGo(case_num: int, N: int, M: int, a_list: List[int], b_list: List[int], ans: int) -> None: 
    res = joyGo(N, M, a_list, b_list)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ