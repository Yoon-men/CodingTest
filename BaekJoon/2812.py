# 백준2812 : 크게 만들기
import sys; input = sys.stdin.readline

def joyGo(N: int, K: int, num: int) -> int: 
    stack = []
    num = [int(i) for i in list(str(num))]

    for i in range(N): 
        while (stack) and (K > 0) and (stack[-1] < num[i]): 
            stack.pop()
            K -= 1
        stack.append(num[i])
    
    return int(''.join(map(str, stack[:len(stack)-K])))


if __name__ == "__main__": 
    N, K = map(int, input().split())
    num = input().strip()

    print(joyGo(N, K, num))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, K, num, ans"), 
    [
        (1, 4, 2, 1924, 94), 
        (2, 7, 3, 1231234, 3234), 
        (3, 10, 4, 4177252841, 775841), 
        (4, 5, 2, 54321, 543)
    ]
)

def test_joyGo(case_num: int, N: int, K: int, num: int, ans: int) -> None: 
    res = joyGo(N, K, num)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ