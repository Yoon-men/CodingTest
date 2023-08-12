# 백준1253 : 좋다
import sys; input = sys.stdin.readline

def joyGo(N: int, nums: list) -> int : 
    ans = []
    nums.sort()

    for i in range(N) : 
        Li = nums[:i] + nums[i+1:]
        s, e = 0, len(Li)-1
        while s < e : 
            num = Li[s] + Li[e]
            if num == nums[i] : 
                ans.append(num)
                break

            if num < nums[i] : s += 1
            else : e -= 1


    return len(ans)



if __name__ == "__main__" : 
    N = int(input())
    nums = list(map(int, input().split()))

    print(joyGo(N, nums))