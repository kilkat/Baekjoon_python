num = int(input())
sum = [0 for i in range(num)]
cnt = 0

for i in sum:
    a, b = map(int, input().split())
    sum[cnt] = a + b
    cnt += 1

for i in range(num):
    print("Case #"+ str(i + 1) +": " + str(sum[i]))