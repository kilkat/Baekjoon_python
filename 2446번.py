a = int(input())
cnt = 0
space = 0
space_2 = 2
dec = 1
dec_2 = 3
for i in range(0, a):
    print(' ' * space, end = '')
    print('*' * (2 * a - dec))
    space += 1
    dec += 2
for i in range(0, a - 1):
    print(' ' *  (a - space_2), end = '')
    print('*' * (a - (a - dec_2)))
    space_2 += 1
    dec_2 += 2