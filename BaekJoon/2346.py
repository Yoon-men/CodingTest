# 백준2346 : 풍선 터뜨리기
from collections import deque
N = int(input())
dq = deque(enumerate(map(int, input().split())))
ans = []
while dq : 
    idx, num = dq.popleft()
    ans.append(idx+1)
    if num>0 : dq.rotate(-(num-1))
    else : dq.rotate(-num)
print(*ans)