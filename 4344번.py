n = int(input())
for i in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]
    cnt = 0
    for scores in nums[1:]:
        if scores > avg:
            cnt += 1
    rate = cnt / nums[0] * 100
    print(str(format(rate, '.3f')+'%'))