# 백준16165 : 걸그룹 마스터 준석이
import sys
input = sys.stdin.readline

groups, celebrity = {}, {}
N, M = map(int, input().split())

for _ in range(N) : 
    group = input().strip()
    groups[group] = []
    for __ in range(int(input())) : 
        member = input().strip()
        groups[group].append(member)
        celebrity[member] = group

for _ in range(M) : 
    quiz = input().strip()
    quizType = int(input())
    print(celebrity[quiz] if quizType == 1 else "\n".join(sorted(groups[quiz])))