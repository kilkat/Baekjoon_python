a = int(input())
cnt = 0
space = a - 1
for i in range(0 , a):
    print(' ' * (space - cnt), end = '')
    print('*' * ((2 * cnt) + 1))
    cnt += 1