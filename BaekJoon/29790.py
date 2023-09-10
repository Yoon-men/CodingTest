# 백준29790 : 임스의 메이플컵
N, U, L = map(int, input().split())
print("Very Good" if ((N >= 1000) and ((U >= 8000) or (L >= 260))) else "Good" if (N >= 1000) else "Bad")