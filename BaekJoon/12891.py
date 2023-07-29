# 백준12891 : DNA 비밀번호
import sys; input = sys.stdin.readline

def joyGo(S: int, P: int, D: list, restriction: list) -> int : 
    ans = 0
    
    A, C, G, T = restriction
    cnt_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for word in D[:P] : cnt_dict[word] += 1
    if (cnt_dict['A'] >= A) and (cnt_dict['C'] >= C) and (cnt_dict['G'] >= G) and (cnt_dict['T'] >= T) : 
        ans += 1

    for i in range(1, S-P+1) : 
        cnt_dict[D[i-1]] -= 1
        cnt_dict[D[i+P-1]] += 1
        if (cnt_dict['A'] >= A) and (cnt_dict['C'] >= C) and (cnt_dict['G'] >= G) and (cnt_dict['T'] >= T) : 
            ans += 1
    
    return ans


if __name__ == "__main__" : 
    S, P = map(int, input().split())
    D = list(input().strip())
    restriction = list(map(int, input().split()))

    print(joyGo(S, P, D, restriction))