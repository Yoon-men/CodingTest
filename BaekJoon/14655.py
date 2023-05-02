# 백준14655 : 욱제는 도박쟁이야!!
_ = int(input())
print(sum(map(lambda x: abs(int(x)), input().split())) + sum(map(lambda x: abs(int(x)), input().split())))