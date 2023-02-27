C, K, P = map(int, input().split())
cnt = 0
while True:
    if C == 0:
        break
    cnt += (K*C)+(P*C*C)
    C -= 1
print(cnt)