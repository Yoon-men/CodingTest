# 백준1009 : 분산처리
import sys
input = sys.stdin.readline

def shit(x, y) : 
    x %= 10
    y %= len(f[x])
    return f[x][y-1]

if __name__ == "__main__" : 
    f = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
    for _ in range(int(input())) : 
        a, b = map(int, input().split())
        print(shit(a, b))