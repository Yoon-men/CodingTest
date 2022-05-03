# 거스름돈
money = 1000 - int(input())
cnt = 0
change = [500, 100, 50, 10, 5, 1]
for i in change : 
    changeNum = money//i
    money -= i*changeNum
    cnt += changeNum
print(cnt)