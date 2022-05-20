# 킹, 퀸, 룩, 비숍, 나이트, 폰
correct = [1, 1, 2, 2, 2, 8]
piece = list(map(int, input().split()))
print(" ".join(str(correct[i] - piece[i]) for i in range(6)))