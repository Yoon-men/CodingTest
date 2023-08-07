# 백준11815 : 짝수? 홀수?
_ = input()
ans_list = [1 if num == int(num**0.5)**2 else 0 for num in list(map(int, input().split()))]
print(*ans_list)