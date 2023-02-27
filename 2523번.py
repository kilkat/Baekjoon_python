a = int(input())
cnt = 1
cnt_2 = 1
for i in range(0, a):
    print('*' * cnt)
    cnt += 1
for i in range(0 , a - 1):
    print('*' * (a - cnt_2))
    cnt_2 += 1