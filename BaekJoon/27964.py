# 백준27964 : 콰트로치즈피자
import sys; input = sys.stdin.readline
_ = input()
Se = set([item for item in input().split() if (len(item) >= 6 and item[-6:] == "Cheese")])
print("yummy" if (len(Se) >= 4) else "sad")