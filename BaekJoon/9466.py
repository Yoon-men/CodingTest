# 백준9466 : 텀 프로젝트
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def joyGo(n: int, Li: list) -> int : 
    def DFS(person: int) -> None : 
        global ans_list, cycle_list
        visited[person] = 1
        cycle_list.append(person)

        next = Li[person]
        if visited[next] : 
            if next in cycle_list : 
                ans_list += cycle_list[cycle_list.index(next):]
                # ㅠㅠㅠㅠㅠㅠ < Test code / please lock the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
                # print(f"[system] cycle_list: {cycle_list}")
                # print(f"[system] ans_list: {ans_list}")
                # ㅛㅛㅛㅛㅛㅛ < Test code / please lock the contents of this lines. > ㅛㅛㅛㅛㅛㅛ
            return
        
        DFS(next)


    global ans_list
    ans_list = []
    Li = [0] + Li
    visited = [0] * (n+1)

    for i in range(1, n+1) : 
        if not visited[i] : 
            global cycle_list
            cycle_list = []
            DFS(i)

    return n - len(ans_list)



if __name__ == "__main__" : 
    for _ in range(int(input())) : 
        n = int(input())
        Li = list(map(int, input().split()))

        print(joyGo(n, Li))

    # # ㅠㅠㅠㅠㅠㅠ < Test code / please lock the contents of this lines. > ㅠㅠㅠㅠㅠㅠ
    # n = 7
    # Li = [3,1,3,7,3,4,6]
    # print(joyGo(n, Li))         # ans = 3

    # n = 8
    # Li = [1,2,3,4,5,6,7,8]
    # print(joyGo(n, Li))         # ans = 0
    # # ㅛㅛㅛㅛㅛㅛ < Test code / please lock the contents of this lines. > ㅛㅛㅛㅛㅛㅛ