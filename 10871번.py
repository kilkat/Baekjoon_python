num1, num2 = map(int, input().split())
cnt = 0
num3 = list(map(int, input().split()))
for i in range(0, num1):
    if num2 > num3[cnt]:
        print(num3[cnt], end=' ')
    cnt += 1