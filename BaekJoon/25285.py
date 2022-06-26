# 백준25285 : 심준의 병역판정검사
import sys
input = sys.stdin.readline

slaveNum = int(input())
for _ in range(slaveNum) : 
    H, W = map(int, input().split())
    BMI = W/(H/100)**2
    if H < 140.1 : 
        print(6)
    elif H < 146 : 
        print(5)
    elif H < 159 : 
        print(4)
    elif H < 161 : 
        if 16 <= BMI < 35 : 
            print(3)
        else : 
            print(4)
    elif H < 204 : 
        if 20 <= BMI < 25 : 
            print(1)
        elif 18.5 <= BMI < 20 or 25 <= BMI < 30 : 
            print(2)
        elif 16 <= BMI < 18.5 or 30 <= BMI < 35 : 
            print(3)
        else : 
            print(4)
    else : 
        print(4)