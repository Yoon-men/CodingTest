# 파티가 끝나고 난 뒤
import sys
input = sys.stdin.readline
man, area = map(int, input().split())
article = list(map(int, input().split()))
print(" ".join(str(i - man*area) for i in article))