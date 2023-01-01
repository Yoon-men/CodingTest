# 백준15652 : N과 M (4)
def joyGo(node) : 
    if len(box) == M : 
        print(" ".join(map(str, box)))
        return

    for i in range(node, N+1) : 
        box.append(i)
        joyGo(i)
        box.pop()

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    box = []
    joyGo(1)