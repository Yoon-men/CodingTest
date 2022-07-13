# 백준25318 : solved.ac 2022
from datetime import datetime
import sys
input = sys.stdin.readline


def main() : 
    N = int(input())
    if N == 0 : 
        return 0

    recordLi = []
    for _ in range(N) : 
        Day, Time, Difficulty = map(str, input().split())
        record = datetime.strptime(f"{Day} {Time}", "%Y/%m/%d %H:%M:%S")
        recordLi.append([record, int(Difficulty)])

    t_N = recordLi[-1][0]
    calcLi = [max(0.5**((t_N-recordLi[i][0]).seconds/(365*24*60*60) + (t_N-recordLi[i][0]).days/365), 0.9**(N-(i+1))) for i in range(N)]
    answer = 0
    for i in range(N) : 
        answer += calcLi[i] * recordLi[i][1]
    answer = round(answer/sum(calcLi))

    return answer


if __name__ == "__main__" : 
    print(main())