# 백준9536 : 여우는 어떻게 울지?
import sys; input = sys.stdin.readline
from typing import List, Set

def joyGo(record: List[str], voice_set: Set[str]) -> str: 
    ans = []
    for voice in record: 
        if not voice in voice_set: 
            ans.append(voice)
    
    return ' '.join(ans)


if __name__ == "__main__": 
    for _ in range(int(input())): 
        record = input().split()
        voice_set = set()
        while True: 
            knowledge = input().strip()
            if knowledge == "what does the fox say?": break

            voice_set.add(knowledge.split()[-1])
        
        print(joyGo(record, voice_set))



# ㅠㅠㅠㅠㅠㅠ < Test code / please ignore this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, record, voice_set, ans"), 
    [
        (
            1,
            "toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot".split(), 
            {'toot', 'blub', 'woof', 'ow'}, 
            "wa pa pa pa pa pa pow"
        )
    ]
)

def test_joyGo(case_num: int, record: List[str], voice_set: Set[str], ans: str) -> None: 
    res = joyGo(record, voice_set)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please ignore this lines. > ㅛㅛㅛㅛㅛㅛ