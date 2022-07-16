# 백준1676 : 팩토리얼 0의 개수
import sys

def factorial(n) : 
    if n == 0 : 
        return 1
    elif n >= 1 : 
        return factorial(n-1) * n

if __name__ == "__main__" : 
    answer = 0
    for i in str(factorial(int(sys.stdin.readline())))[::-1] : 
        if i != "0" : 
            break
        answer += 1
    print(answer)