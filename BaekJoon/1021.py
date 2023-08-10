# 백준1021 : 회전하는 큐
import sys; input = sys.stdin.readline
from collections import deque

def joyGo(N: int, nums: list) -> int : 
    ans = 0
    Li = deque([i for i in range(1, N+1)])

    for num in nums : 
        while True : 
            if Li[0] == num : 
                Li.popleft()
                break
            else : 
                if Li.index(num) < len(Li)/2 : 
                    Li.append(Li.popleft())
                    ans += 1
                else : 
                    Li.appendleft(Li.pop())
                    ans += 1
    
    return ans


if __name__ == "__main__" : 
    N, _ = map(int, input().split())
    nums = list(map(int, input().split()))

    print(joyGo(N, nums))