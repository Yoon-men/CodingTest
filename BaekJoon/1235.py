# 백준1235 : 학생 번호
import sys ; input = sys.stdin.readline

def solve(Li) : 
    for idx in range(1, len(Li[0])+1) : 
        chkLi = [i[:idx] for i in Li]
        if len(Li) == len(set(chkLi)) : 
            return idx

if __name__ == "__main__" : 
    N = int(input())
    Li = [input().strip()[::-1] for _ in range(N)]
    print(solve(Li))