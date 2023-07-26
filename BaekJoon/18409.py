# 백준18409 : 母音を数える (Counting Vowels)
def joyGo(S: str) -> int : 
    cnt = 0
    for i in S : 
        if i in {'a', 'i', 'u', 'e', 'o'} : cnt += 1
    
    return cnt


if __name__ == "__main__" : 
    _ = int(input())
    S = input()

    print(joyGo(S))