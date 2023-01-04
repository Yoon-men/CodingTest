# 백준15657 : N과 M (8)
import sys; input = sys.stdin.readline

def joyGo(node) : 
    if len(box) == M : 
        print(*box)
        return
    for i in range(node, N) : 
        box.append(Li[i])
        joyGo(i)
        box.pop()

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = sorted(list(map(int, input().split())))
    box = []
    joyGo(0)