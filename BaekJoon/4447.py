# 백준4447 : 좋은놈 나쁜놈
import sys ; input = sys.stdin.readline
for _ in range(int(input())) : 
    s = input().strip()
    gNum = s.count("g") + s.count("G")
    bNum = s.count("b") + s.count("B")
    print(f"{s} is {'GOOD' if gNum > bNum else 'NEUTRAL' if gNum == bNum else 'A BADDY'}")