a1 = int(input())
a2 = int(input())
a3 = int(input())
mul = list(str(a1 * a2 * a3))
for i in range(10):
    print(mul.count(str(i)))