# 백준30034 : Slice String
from typing import Set, List

def separate(s: str, separator_set: Set[str]) -> List[str] : 
    tmp, ans = [], s.split()
    for i in separator_set : 
        tmp = ans[:]
        tmp, ans = ans[:], []
        for j in tmp : 
            ans.extend(j.split(i))

    return ans            


if __name__ == "__main__" : 
    _ = input()
    separator_set = set()
    for i in input().split() : separator_set.add(i)
    _ = input()
    for i in input().split() : separator_set.add(i)
    _ = input()
    for i in input().split() : separator_set.discard(i)
    _ = input()
    s = input()

    for i in separate(s, separator_set) : 
        if i : print(i)