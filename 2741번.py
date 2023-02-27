n = int(input())
Num = 0
cnt = 0
a = 1
while True:
    Num = n - (n - a)
    a += 1
    cnt += 1
    print(Num)
    if cnt >= n:
        break