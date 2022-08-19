# 백준1822 : 차집합
_ = input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
answer = sorted(A - B)
print(len(answer))
if len(answer) != 0 : 
    print(*answer)