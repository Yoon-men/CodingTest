# 백준2309 : 일곱 난쟁이
import sys ; input = sys.stdin.readline
def joyGo() : 
    for i in range(9) : 
        for j in range(1, 9) : 
            if sum(Li)-Li[i]-Li[j]==100 : 
                a, b = Li[i], Li[j]
                Li.remove(a) ; Li.remove(b)
                for i in Li : print(i)
                return
if __name__ == "__main__" : 
    Li = sorted([int(input()) for _ in range(9)])
    joyGo()