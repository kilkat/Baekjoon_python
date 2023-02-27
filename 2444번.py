a = int(input())
cnt = 0
inc = 0
dec = 3
space = a - 1
for i in range(0, a):
    print(' ' * (space - cnt), end = '')
    print('*' * (a - (a - inc) + 1))
    cnt += 1
    inc += 2
for i in range(0 , a - 1):
    print(' ' * (a - space), end = '')
    print('*' * ((a * 2)-dec))
    dec += 2
    space -= 1