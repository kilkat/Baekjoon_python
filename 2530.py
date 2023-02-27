a = input().split()
b = int(input())
hour = int(a[0])
min = int(a[1])
sec = int(a[2])

sec += b
min += sec // 60
sec %= 60

hour += min // 60
min %= 60

hour %= 24

print(str(hour) + ' ' + str(min) + ' ' + str(sec))