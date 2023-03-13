# 백준5355 : 화성 수학
import sys; input = sys.stdin.readline

for _ in range(int(input())) : 
    Li = input().split(); ans = float(Li[0])
    for operator in Li[1:] : 
        if operator == "@" : ans *= 3
        elif operator == "%" : ans += 5
        else : ans -= 7
    print(f"{ans:.2f}")