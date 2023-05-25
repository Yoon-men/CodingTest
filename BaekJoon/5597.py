# 백준5597 : 과제 안 내신 분..?
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> list : 
    ans_list = [i for i in range(1, 31) if i not in Li]
    return ans_list


if __name__ == "__main__" : 
    Li = [int(input()) for _ in range(28)]
    print("\n".join(map(str, joyGo(Li))))