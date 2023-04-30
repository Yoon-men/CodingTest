# 백준13414 : 수강신청
import sys; input = sys.stdin.readline

def joyGo(K: int, L: int, Li: list) -> None : 
    Di = {student_no: idx for idx, student_no in enumerate(Li)} 
    ansLi = sorted(Di.items(), key=lambda x: x[1])

    if K > len(ansLi) : K = len(ansLi)
    print("\n".join((ansLi[i][0] for i in range(K))))


if __name__ == "__main__" : 
    K, L = map(int, input().split())
    Li = [input().strip() for _ in range(L)]
    joyGo(K, L, Li)