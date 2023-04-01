# 백준2979 : 트럭 주차
import sys; input = sys.stdin.readline
from collections import defaultdict

def joyGo(parking_price: list, parking_time: list) -> int : 
    cnt_by_time = defaultdict(int)
    total_price = 0

    for enter_time, leave_time in parking_time : 
        for time in range(enter_time, leave_time) : 
            cnt_by_time[time] += 1

    for time in cnt_by_time.values() : 
        total_price += time*parking_price[time]

    return total_price

if __name__ == "__main__" : 
    parking_price = [0] + list(map(int, input().split()))
    parking_time = [list(map(int, input().split())) for _ in range(3)]

    print(joyGo(parking_price, parking_time))