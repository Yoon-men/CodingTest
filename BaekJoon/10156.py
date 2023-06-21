# 백준10156 : 과자
def joyGo(K: int, N: int, M: int) -> int : 
    return K*N - M if (K*N > M) else 0

if __name__ == "__main__" : 
    K, N, M = map(int, input().split())
    print(joyGo(K, N, M))