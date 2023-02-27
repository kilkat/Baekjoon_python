num = input().split()
mul = int(num[0]) * int(num[1])
cnt = int(0)

while cnt < mul:
    sum = mul - cnt
    cnt += 1

print(cnt - 1)