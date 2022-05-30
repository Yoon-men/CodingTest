# 백준15650 : N과 M (2)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
storage = []


def detection(start) : 
    if len(storage) == M : 
        print(" ".join(map(str, storage)))
        return
    
    for i in range(start, N+1) : 
        if i not in storage : 
            storage.append(i)
            detection(i+1)
            storage.pop()


if __name__ == "__main__" : 
    detection(1)