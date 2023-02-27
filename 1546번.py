sum = 0
N = int(input())
a = list(map(int, input().split()))
top = max(a)
for i in range(0, N):
    sum += a[i] / top * 100
print(sum / N)