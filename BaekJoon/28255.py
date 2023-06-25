# 백준28255 : 3단 초콜릿 아이스크림
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> list : 
    def check(s: str) -> int : 
        s_prefix_len = (len(s)+2) // 3
        s_prefix = s[:s_prefix_len]
        def rev(S: str) -> str : 
            return S[::-1]
        def tail(S: str) -> str : 
            return S[1:]

        if s == s_prefix + rev(s_prefix) + s_prefix :
            return 1
        elif s == s_prefix + tail(rev(s_prefix)) + s_prefix :
            return 1
        elif s == s_prefix + rev(s_prefix) + tail(s_prefix) :
            return 1
        elif s == s_prefix + tail(rev(s_prefix)) + tail(s_prefix) :
            return 1

        return 0


    return [check(s) for s in Li]


if __name__ == "__main__" : 
    Li = [input().strip() for _ in range(int(input()))]
    print(*joyGo(Li), sep='\n')