# 백준1448 : 삼각형 만들기
import sys
input = sys.stdin.readline

def joyGo(l) : 
    for i in range(len(l)-2) : 
        if l[i] < l[i+1] + l[i+2] : 
            return l[i] + l[i+1] + l[i+2]
    return -1

if __name__ == "__main__" : 
    lengths = []
    for _ in range(int(input())) : 
        lengths.append(int(input()))
    lengths.sort(reverse=True)
    print(joyGo(lengths))