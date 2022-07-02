# 백준2447 : 별 찍기 - 10
import sys

def drawingStar(n) : 
    if n == 3 : 
        return ["***", "* *", "***"]
    
    starList = drawingStar(n//3)
    stars = []

    for i in starList : 
        stars.append(i * 3)
    
    for i in starList : 
        stars.append(i + " "*(n//3) + i)
    
    for i in starList : 
        stars.append(i*3)
    
    return stars

if __name__ == "__main__" : 
    N = int(sys.stdin.readline())
    print("\n".join(drawingStar(N)))