num = (input().split())
n = int(num[0])
r = int(num[1])
c = n - r
numerator = 1
denominator = 1
for i in range(1, n + 1):
    numerator *= i # 계산값 = 120
for i2 in range(1, r + 1):
    denominator *= i2 # 계산값 = 2
for i3 in range(1, c + 1):
    denominator *= i3 # 계산값 = 6
print(numerator // denominator)