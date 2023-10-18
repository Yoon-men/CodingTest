# 백준4659 : 비밀번호 발음하기
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(pw: str) -> None : 
    byebye = lambda pw: print(f"<{pw}> is not acceptable.")
    vowel = ('a', 'e', 'i', 'o', 'u')

    for char in vowel : 
        if char in set(pw) : break
    else : byebye(pw); return
    
    if len(pw) > 2 : 
        pw_checker = deque(pw[:3])
        if all(pw_checker[i] in vowel for i in range(3)) : byebye(pw); return
        elif all(not pw_checker[i] in vowel for i in range(3)) : byebye(pw); return
        for i in range(3, len(pw)) : 
            pw_checker.popleft()
            pw_checker.append(pw[i])
            if all(pw_checker[i] in vowel for i in range(3)) : byebye(pw); return
            elif all(not pw_checker[i] in vowel for i in range(3)) : byebye(pw); return
    if len(pw) > 1 : 
        duplicate_exception = ['e', 'o']
        for i in range(len(pw)-1) : 
            pw_checker = set(pw[i:i+2])
            if len(set(pw_checker)) == 1 : 
                if not list(pw_checker)[0] in duplicate_exception : byebye(pw); return

    print(f"<{pw}> is acceptable.")


if __name__ == "__main__" : 
    while True : 
        pw = input().strip()
        if pw == "end" : break
        else : joyGo(pw)