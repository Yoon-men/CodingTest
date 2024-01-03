# 백준30970 : 선택의 기로
import sys; input = sys.stdin.readline

Li = [list(map(int, input().split())) for _ in range(int(input()))]

Li_1 = sorted(Li, key=lambda x: (-x[0], x[1]))
Li_2 = sorted(Li, key=lambda x: (x[1], -x[0]))

print(*Li_1[0], *Li_1[1])
print(*Li_2[0], *Li_2[1])