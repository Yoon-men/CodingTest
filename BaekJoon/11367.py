# 백준11367 : Report Card Time
for _ in range(int(input())) : 
    a, b = input().split()
    b = int(b)
    print(f"{a} {'A+' if (97 <= b <= 100) else 'A' if (90 <= b <= 96) else 'B+' if (87 <= b <= 89) else 'B' if (80 <= b <= 86) else 'C+' if (77 <= b <= 79) else 'C' if (70 <= b <= 76) else 'D+' if (67 <= b <= 69) else 'D' if (60 <= b <= 66) else 'F'}")