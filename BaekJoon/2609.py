# 최대공약수와 최소공배수
A, B = map(int, input().split())
a, b = A, B
while b != 0 : 
    c = a%b
    a = b
    b = c
GCD = a                     # Great Common Divisor = GCD = 최대공약수
LCM = A*B // GCD            # Largest Common Multiple = LCM = 최소공배수
print(GCD)
print(LCM)