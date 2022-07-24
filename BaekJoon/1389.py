# 백준1389 : 케빈 베이컨의 6단계 법칙
from collections import deque
import sys
input = sys.stdin.readline

def check(person) : 
    checkLi = deque([person])
    visited[person-1] = 1

    while checkLi : 
        obj = checkLi.popleft()
        for i in people[obj-1] : 
            if visited[i-1] == 0 : 
                visited[i-1] = visited[obj-1] + 1
                checkLi.append(i)
    

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    people = [[] for _ in range(N)]
    for i in range(M) : 
        A, B = map(int, input().split())
        people[A-1].append(B)
        people[B-1].append(A)
    
    answerLi = []
    for man in range(N) : 
        visited = [0] * N
        check(man+1)
        answerLi.append(sum(visited))

    print(answerLi.index(min(answerLi)) + 1)