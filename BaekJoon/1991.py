# 백준1991 : 트리 순회
import sys; input = sys.stdin.readline

def joyGo(graph_dict: dict) -> list : 
    ans_list = [[] for _ in range(3)]

    def preorder(root) : 
        if root != '.' : 
            left, right = graph_dict[root][0], graph_dict[root][1]
            ans_list[0].append(root)
            preorder(left)
            preorder(right)
    def inorder(root) : 
        if root != '.' : 
            left, right = graph_dict[root][0], graph_dict[root][1]
            inorder(left)
            ans_list[1].append(root)
            inorder(right)
    def postorder(root) : 
        if root != '.' : 
            left, right = graph_dict[root][0], graph_dict[root][1]
            postorder(left)
            postorder(right)
            ans_list[2].append(root)
    
    preorder('A')
    inorder('A')
    postorder('A')

    return ans_list


if __name__ == "__main__" : 
    N = int(input())
    graph_dict = {}
    for _ in range(N) : 
        root, left, right = input().split()
        graph_dict[root] = [left, right]
    for line in joyGo(graph_dict) : 
        print(''.join(line))