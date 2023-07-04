# 백준2740 : 행렬 곱셈
import sys; input = sys.stdin.readline

def joyGo(N: int, M: int, K: int, mat_1: list, mat_2: list) : 
    ans_mat = [[0 for _ in range(K)] for _ in range(N)]
    
    for i in range(N) : 
        for j in range(K) : 
            for k in range(M) : 
                ans_mat[i][j] += mat_1[i][k] * mat_2[k][j]

    return ans_mat


if __name__ == "__main__" : 
    N, M = map(int, input().split())
    mat_1 = [list(map(int, input().split())) for _ in range(N)]
    M, K = map(int, input().split())
    mat_2 = [list(map(int, input().split())) for _ in range(M)]

    ans_mat = joyGo(N, M, K, mat_1, mat_2)
    for row in ans_mat : 
        print(*row)