while True:
    a, b, c = input().split()
    listup = [int(a), int(b), int(c)]
    listup.sort()
    if listup[0] + listup[1] + listup[2] == 0:
        break
    if listup[2] ** 2 == listup[0] ** 2 + listup[1] ** 2:
        print('right')
    else:
        print('wrong')