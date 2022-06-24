# 백준23254 : 나는 기말고사형 인간이야
import heapq as hq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
scoreMin = list(map(int, input().split()))
scorePlus = list(map(int, input().split()))


subjects = []
for i in range(M) : 
    hq.heappush(subjects, [-scorePlus[i], scoreMin[i]])

hours = N * 24

while subjects[0][0] != 0 and hours > 0 : 
    maxHeap = hq.heappop(subjects)
    sp, sm = -maxHeap[0], maxHeap[1]

    time = (100-sm) // sp
    
    if hours >= time : 
        hours -= time
    else : 
        time = hours
        hours = 0

    sm = time*sp + sm
    sp = 100 - sm

    hq.heappush(subjects, [-sp, sm])


scoreSum = 0
for i in subjects : 
    scoreSum += i[1]
print(scoreSum)