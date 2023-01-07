# 백준15666 : N과 M (12)
def joyGo(s) : 
    if len(box) == M : 
        print(*box)
        return
    
    before = 0
    for i in range(s, N) : 
        if before != Li[i] : 
            box.append(Li[i])
            before = Li[i]
            joyGo(i)
            box.pop()


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = sorted(list(map(int, input().split())))

    box = []
    joyGo(0)