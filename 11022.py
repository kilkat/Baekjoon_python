num = int(input())
lst = [0 for i in range(num * 2)]
sum = [0 for i in range(num)]
cnt = 0
cnt2 = 0
cnt3 = 0

for i in range(num):
    a, b = map(int, input().split())
    lst[cnt2] = a
    lst[cnt2 + 1] = b
    sum[cnt] = a + b
    cnt2 += 2
    cnt += 1

for i in range(num):
    print("Case #"+ str(i + 1) +": " + str(lst[cnt3]) + " + " + str(lst[cnt3 + 1]) + " = " + str(sum[i]))
    cnt3 += 2