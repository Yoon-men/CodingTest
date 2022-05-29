# 백준15649 : N과 M (1)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
storage = []


def detection() : 
    if len(storage) == M : 
        print(" ".join(map(str, storage)))
        return
    
    for i in range(1, N+1) : 
        if i not in storage : 
            storage.append(i)
            detection()
            storage.pop()


if __name__ == "__main__" : 
    detection()