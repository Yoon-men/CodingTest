# 백준17071 : 숨바꼭질 5
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, K: int) -> int: 
    MAX_LIMIT = 5 * 10**5

    visited = [[-1, -1] for _ in range(MAX_LIMIT + 1)]
    visited[N][0] = 0
    dq = deque([(N, 0)])
    while dq: 
        x, time = dq.popleft()
        brother = K + ((time * (time+1)) // 2)
        if brother > MAX_LIMIT: 
            return -1
        elif visited[brother][time % 2] != -1: 
            return time
        
        for next in (x-1, x+1, x*2): 
            if (0 <= next <= MAX_LIMIT) and (visited[next][(time+1) % 2] == -1): 
                dq.append((next, time+1))
                visited[next][(time+1) % 2] = time

    return -1


if __name__ == "__main__": 
    N, K = map(int, input().split())
    print(joyGo(N, K))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("case_num, N, K, ans"), 
    [
        (1, 5, 17, 2), 
        (2, 17, 5, 4), 
        (3, 6, 6, 0), 
        (4, 1, 500000, -1), 
        (5, 250000, 499999, 1), 
        (6, 1, 10, 6), 
        (7, 8725, 328744, -1), 
        (8, 27297, 339652, 425), 
        (9, 34768, 292340, -1), 
        (10, 438, 129118, 95), 
        (11, 4040, 160532, 385), 
        (12, 6, 0, 4), 
        (13, 7, 37, 5), 
        (14, 10, 57, 5),
        (15, 6, 0, 4), 
        (16, 21, 70, 4), 
        (17, 18, 58, 4), 
        (18, 18, 66, 4), 
        (19, 16, 50, 4), 
        (20, 34, 0, 8)
    ]
)

def test_joyGo(case_num: int, N: int, K: int, ans: int) -> None: 
    res = joyGo(N, K)
    assert res == ans, f"Test case {case_num} - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete this lines. > ㅛㅛㅛㅛㅛㅛ