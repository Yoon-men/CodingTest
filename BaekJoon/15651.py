# 백준15651 : N과 M (3)
def joyGo() : 
    if len(box)==M : print(*box) ; return
    for i in range(1, N+1) : 
        box.append(i)
        joyGo()
        box.pop()

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    box = []
    joyGo()