# 백준1715 : 카드 정렬하기
import sys; input = sys.stdin.readline
from queue import PriorityQueue

que = PriorityQueue()
for _ in range(int(input())) : 
    que.put(int(input()))

ans = 0
while que.qsize() > 1 : 
    tmp = que.get() + que.get()
    ans += tmp
    que.put(tmp)

print(ans)