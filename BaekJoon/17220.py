# 백준17220 : 마약수사대
import sys; input = sys.stdin.readline
from typing import Dict, List

def joyGo(N: int, supplier_dict: Dict[str, List[str]], arrested: List[str]) -> int : 
    def DFS(supplier: str) -> None : 
        nonlocal ans
        visited[supplier] = 1
        for demander in supplier_dict[supplier] : 
            if not visited[demander] : 
                ans += 1
                DFS(demander)


    visited = {chr(i): 0 for i in range(65, 65+N)}
    root    = {chr(i): 1 for i in range(65, 65+N)}
    for supplier_list in supplier_dict.values() : 
        for supplier in supplier_list : 
            root[supplier] = 0
    for supplier in arrested : 
        visited[supplier] = 1

    ans = 0
    for i in range(65, 65+N) : 
        if (root[chr(i)]) and (not visited[chr(i)]) : 
            DFS(chr(i))
    
    return ans



if __name__ == "__main__" : 
    N, M = map(int, input().split())
    supplier_dict = {chr(i): [] for i in range(65, 65+N)}
    for _ in range(M) : 
        u, v = input().split()
        supplier_dict[u].append(v)
    _, *arrested = input().split()
    
    print(joyGo(N, supplier_dict, arrested))
