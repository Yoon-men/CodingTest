# 백준9996 : 한국이 그리울 땐 서버에 접속하지
import sys; input = sys.stdin.readline

def joyGo(N: int, pattern: str, Li: list) -> list : 
    pattern_list = pattern.split("*")
    ans_list = ["DA" if ((s[:len(pattern_list[0])] == pattern_list[0]) and (s[-len(pattern_list[-1]):] == pattern_list[-1]) and (len("".join(pattern_list)) <= len(s))) else "NE" for s in Li]
    
    return ans_list


if __name__ == "__main__" : 
    N = int(input())
    pattern = input().strip()
    Li = [input().strip() for _ in range(N)]
    print("\n".join(joyGo(N, pattern, Li)))