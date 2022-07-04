# 백준2309 : 일곱 난쟁이
import sys
def check(h) : 
    for i in range(9) : 
        for j in range(1, 9) : 
            if sum(h) - h[i] - h[j] == 100 : 
                spy_1 = h[i]
                spy_2 = h[j]
                h.remove(spy_1)
                h.remove(spy_2)
                for i in h : 
                    print(i)
                return
if __name__ == "__main__" : 
    check(sorted([int(sys.stdin.readline()) for _ in range(9)]))