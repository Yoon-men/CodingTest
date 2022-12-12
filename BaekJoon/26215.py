# 백준26215 : 눈 치우기
N = int(input())
Li = sorted(list(map(int, input().split())))
t = 0

while sum(Li) != 0 : 
    if N > 1 : 
        Li[-1] -= Li[-2]
        t += Li[-2]
        Li[-2] = 0
        N -= 1
        Li.sort()
    else : 
        t += Li[-1]
        Li[-1] = 0

print(-1 if t > 1440 else t)