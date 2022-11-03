# 백준1068 : 트리
def joyGo(delNum, li) : 
    li[delNum] = -2
    for i in range(N) : 
        if delNum == li[i] : 
            joyGo(i, li)

if __name__ == "__main__" : 
    N = int(input())
    nodes = list(map(int, input().split()))
    delNode = int(input())

    joyGo(delNode, nodes)

    cnt = 0
    for i in range(N) : 
        if (nodes[i] != -2) and (i not in nodes) : cnt += 1

    print(cnt)