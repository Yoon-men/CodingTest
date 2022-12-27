# 백준16168 : 퍼레이드
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def isEulerianTrail() : 
    oddDegreeCnt = 0
    for i in range(V) : 
        degree = 0
        for j in range(V) : 
            if adjacentMatrix[i][j] : 
                degree += 1
        if degree%2 == 1 : 
            oddDegreeCnt += 1

    if (oddDegreeCnt == 1) or (oddDegreeCnt > 2) : return False
    else : return True

def joyGo(cur) : 
    for i in range(V) : 
        if adjacentMatrix[cur][i] > 0 : 
            adjacentMatrix[cur][i] = 0
            adjacentMatrix[i][cur] = 0
            joyGo(i)


if __name__ == "__main__" : 
    V, E = map(int, input().split())
    adjacentMatrix = [[0]*V for _ in range(V)]
    for _ in range(E) : 
        a, b = map(int, input().split()); a -= 1; b -= 1
        adjacentMatrix[a][b] = 1
        adjacentMatrix[b][a] = 1
    
    if not isEulerianTrail() : 
        print("NO"); sys.exit()
    
    joyGo(0)
    for row in adjacentMatrix : 
        if 1 in row : 
            print("NO"); sys.exit()

    print("YES")