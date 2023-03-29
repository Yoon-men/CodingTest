# 백준14656 : 조교는 새디스트야!!
N = int(input())
Li = list(map(int, input().split()))
sortedLi = sorted(Li)
ans = len([i for i in range(N) if Li[i] != sortedLi[i]])
print(ans)