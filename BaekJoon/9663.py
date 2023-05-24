# 백준9663 : N-Queen
def isAble(n: int) -> bool : 
    for i in range(n) : 
        if (row[n] == row[i]) or (abs(row[n]-row[i]) == n-i) : 
            return False
    return True

def DFS(n: int) -> None : 
    global ans
    if n == N : ans += 1
    else : 
        for i in range(N) : 
            row[n] = i
            if isAble(n) : DFS(n+1)


if __name__ == "__main__" : 
    N = int(input())
    row = [0] * N
    ans = 0
    DFS(0)

    print(ans)