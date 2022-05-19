# 프린터 큐
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) : 
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    finding = [0 for _ in range(N)]
    finding[M] = 1
    count = 0

    while True : 
        if priority[0] == max(priority) : 
            count += 1
            if finding[0] != 1 : 
                del priority[0]
                del finding[0]
            else : 
                print(count)
                break
        
        else : 
            priority.append(priority[0])
            finding.append(finding[0])
            del priority[0]
            del finding[0]