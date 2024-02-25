# 백준30957 : 빅데이터 vs 정보보호 vs 인공지능
import sys; input = sys.stdin.readline
from collections import Counter

def joyGo(survey_data: str) -> str: 
    survey_result = Counter(survey_data)
    _max = max(survey_result.values())
    
    check_dict = {
        'B': 0, 
        'S': 0, 
        'A': 0
    }

    for key, value in survey_result.items(): 
        if value == _max: 
            check_dict[key] = 1
    
    if sum(check_dict.values()) == 3: 
        return "SCU"
    else: 
        ans = ''
        if check_dict['B']: 
            ans += 'B'
        if check_dict['S']: 
            ans += 'S'
        if check_dict['A']: 
            ans += 'A'
    
    return ans
    

if __name__ == "__main__": 
    _ = input()
    survey_data = input().strip()

    print(joyGo(survey_data))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, survey_data, ans"), 
    [
        (
            1, 
            "SBSBA", 
            "BS"
        ), 
        (
            2, 
            'A', 
            'A'
        ), 
        (
            3, 
            "ASBASB", 
            "SCU"
        )
    ]
)

def test_joyGo(case_num: int, survey_data: str, ans: str) -> None: 
    res = joyGo(survey_data)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ