a = int(input())
n = input()
n = list(map(int, n))
sum = 0
cnt = 0
for i in range(a):
    sum += n[cnt]
    cnt += 1 
print(sum)