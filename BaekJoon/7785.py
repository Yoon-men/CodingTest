# 백준7785 : 회사에 있는 사람
import sys; input = sys.stdin.readline

def joyGo(Li: list) -> list : 
    Di = {person: status for person, status in Li}
    ans_list = sorted([person for person, status in Di.items() if status == "enter"], reverse=True)

    return ans_list


if __name__ == "__main__" : 
    Li = [input().split() for _ in range(int(input()))]
    print("\n".join(joyGo(Li)))