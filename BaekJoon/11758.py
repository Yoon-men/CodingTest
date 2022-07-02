# 백준11758 : CCW
import sys

def ccw(p1, p2, p3) : 
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

if __name__ == "__main__" : 
    dots = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
    obj = ccw(dots[0], dots[1], dots[2])
    if obj > 0 : 
        print(1)
    elif obj < 0 : 
        print(-1)
    else : 
        print(0)