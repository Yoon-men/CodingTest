# 백준1544 : 사이클 단어
import sys ; input = sys.stdin.readline

def wordInAnsLi(word) : 
    global ansLi
    for ans in ansLi : 
        if len(ans) == len(word) : 
            for _ in range(len(word)) : 
                if ans == word : return True
                word = f"{word[1:]}{word[0]}"
    return False

if __name__ == "__main__" : 
    inputLi = [input().strip() for _ in range(int(input()))]

    ansLi = []
    for word in inputLi : 
        if not wordInAnsLi(word) : ansLi.append(word)

    print(len(ansLi))