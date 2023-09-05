# 백준1916 : 최소비용 구하기
import sys; input = sys.stdin.readline
from typing import Tuple
from heapq import heappush, heappop

def joyGo(N: int, bus_infos: Tuple[Tuple[int, int, int]], departure: int, arrival: int) -> int : 
    bus_graph = [[] for _ in range(N+1)]
    for current_departure, current_arrival, current_charge in bus_infos : 
        bus_graph[current_departure].append((current_arrival, current_charge))

    charge_list = [sys.maxsize] * (N+1)

    hq = []
    heappush(hq, (0, departure))
    charge_list[departure] = 0

    while hq : 
        current_charge, current_departure = heappop(hq)
        if charge_list[current_departure] < current_charge : continue

        for next_arrival, next_charge in bus_graph[current_departure] : 
            total_charge = current_charge + next_charge

            if charge_list[next_arrival] > total_charge : 
                heappush(hq, (total_charge, next_arrival))
                charge_list[next_arrival] = total_charge

    return charge_list[arrival]


if __name__ == "__main__" : 
    N = int(input())
    bus_infos = tuple(tuple(map(int, input().split())) for _ in range(int(input())))
    departure, arrival = map(int, input().split())

    print(joyGo(N, bus_infos, departure, arrival))