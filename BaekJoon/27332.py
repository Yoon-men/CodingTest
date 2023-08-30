# 백준27332 : 11月 (November)
import sys; input = sys.stdin.readline
from datetime import datetime, timedelta

def joyGo(A: int, B: int) -> int : 
    future_day = datetime(2022, 11, A) + timedelta(weeks=B)
    return 1 if (future_day.year == 2022) and (future_day.month == 11) else 0


if __name__ == "__main__" : 
    A = int(input())
    B = int(input())

    print(joyGo(A, B))