# 백준1744 : 수 묶기
import sys; input = sys.stdin.readline

def joyGo(N: int, Li: list) -> int : 
    ans = 0
    p_list, m_list = [], []

    for i in Li : 
        if i == 1 : ans += 1
        elif i > 1 : p_list.append(i)
        else : m_list.append(i)
    p_list.sort(reverse=True)
    m_list.sort()

    for i in range(0, len(p_list), 2) : 
        ans += p_list[i] if i == len(p_list)-1 else p_list[i]*p_list[i+1]
    for i in range(0, len(m_list), 2) : 
        ans += m_list[i] if i == len(m_list)-1 else m_list[i]*m_list[i+1]

    return ans


if __name__ == "__main__" : 
    N = int(input())
    Li = [int(input()) for _ in range(N)]
    print(joyGo(N, Li))