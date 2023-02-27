a = int(input())
cnt = 0
while True:
    time = 0
    avg = 0
    d = 0
    cnt += 1
    if cnt > a:
        break
    n = int(input())
    for i in range(0, n):
        b, c = list(map(float, input().split()))
        d += b * c
        time += b
        avg = d / time 
    print(int(time), round(avg, 1))
    