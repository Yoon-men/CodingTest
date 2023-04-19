# 백준9506 : 약수들의 합
import sys; input = sys.stdin.readline

def joyGo(n: int) -> None : 
    Li = []
    for i in range(1, n) : 
        if n%i == 0 : Li.append(i)
    
    print(f"{n} = {' + '.join(map(str, Li))}" if n == sum(Li) else f"{n} is NOT perfect.")


if __name__ == "__main__" : 
    while True : 
        n = int(input())
        if n == -1 : break
        joyGo(n)