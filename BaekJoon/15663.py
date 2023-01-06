# 백준15663 : N과 M (9)
def joyGo() : 
    if len(box) == M : 
        print(*box)
        return

    before = 0
    for i in range(N) : 
        if (not visited[i]) and (before != Li[i]) : 
            visited[i] = 1
            box.append(Li[i])
            before = Li[i]
            joyGo()
            visited[i] = 0
            box.pop()


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    Li = sorted(list(map(int, input().split())))

    visited = [0] * N
    box = []
    joyGo()