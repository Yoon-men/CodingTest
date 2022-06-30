# 백준5086 : 배수와 약수
import sys
input = sys.stdin.readline


def findingRelationship(a, b) : 
    if b % a == 0 : 
        return "factor"
    elif a % b == 0 : 
        return "multiple"
    else : 
        return "neither"


if __name__ == "__main__" : 
    while True : 
        A, B = map(int, input().split())

        if A == 0 and B == 0 : 
            break

        print(findingRelationship(A, B))