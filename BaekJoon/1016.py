# 백준1016 : 제곱 ㄴㄴ 수
mn, mx = map(int, input().split())
Li = [i**2 for i in range(2, int(mx**0.5)+1)]
nums = [1]*(mx-mn+1)
for i in Li : 
    n = mn//i * i
    while n <= mx : 
        if n-mn >= 0 : 
            nums[n-mn] = 0
            print(f"[ 기열찐빠인 숫자 : {n-mn+1} ]")                # Test code / please delete the contents of this line.
        n += i
print(sum(nums))