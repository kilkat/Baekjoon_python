num = input().split()
cnt, sum = 0, 0
while True:
    sum += int(num[0])
    if sum >= int(num[2]):
        cnt += 1
        break
    sum -= int(num[1])
    if sum >= int(num[2]):
        cnt += 1
        break
    cnt += 1
print(cnt)