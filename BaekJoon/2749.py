# 백준2749 : 피보나치 수 3
import sys; input = sys.stdin.readline

def joyGo(n: int) -> int: 
    MOD = 10**6

    def periodWoOsietekure(m): 
        prev, cur = 0, 1
        for i in range(0, m * m): 
            prev, cur \
            = cur, (prev + cur) % m

            if (prev == 0) and (cur == 1): 
                return i+1


    period = periodWoOsietekure(MOD)
    fibo = [0, 1] + ([-1] * (period - 2))
    for i in range(2, period): 
        fibo[i] = (fibo[i-1] + fibo[i-2]) % MOD
    
    return fibo[n % period]



if __name__ == "__main__": 
    print(joyGo(int(input())))



# ㅠㅠㅠㅠㅠㅠ < Test code / please delete the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
import pytest

@pytest.mark.parametrize(
    ("n, ans"), 
    [
        (1000, 228875)
    ]
)

def test_joyGo(n: int, ans: int) -> None: 
    res = joyGo(n)
    assert res == ans, f"Test Case - 틀렸습니다. (your result: {res} / answer: {ans})"
# ㅛㅛㅛㅛㅛㅛ < Test code / please delete the contents of this lines. > ㅛㅛㅛㅛㅛㅛ