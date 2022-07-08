# 백준18111 : 마인크래프트
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]             # Land
answer = sys.maxsize
H = 0               # Height

for floor in range(257) : 
    maxFloor, minFloor = 0, 0
    
    for i in range(N) : 
        for j in range(M) : 
            if L[i][j] >= floor : 
                maxFloor += L[i][j] - floor
            else : 
                minFloor += floor - L[i][j]

    I = maxFloor + B            # Inventory
    if I < minFloor : 
        continue

    time = 2*maxFloor + minFloor
    if time <= answer : 
        answer = time
        H = floor

print(answer, H)