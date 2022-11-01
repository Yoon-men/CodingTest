# 백준25905 : 장인은 도구를 탓하지 않는다
import sys ; input = sys.stdin.readline
ans = 1
Li = sorted([float(input())for _ in range(10)], reverse=True)
for i in range(9) : 
    ans *= Li[i]/(i+1)
print(ans * 10**9)