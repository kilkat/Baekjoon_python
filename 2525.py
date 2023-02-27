hour, min = input().split()
int_hour = int(hour)
int_min = int(min)
need_time = int(input())

if need_time > 59:
    int_min += need_time
    quota = int(need_time / 60)
    if int_min > 59:
        min_quota = int(int_min / 60)
        int_hour += min_quota
        int_min -= 60 * min_quota
    if int_hour >= 24:
        int_hour -= 24
elif need_time < 60:
    int_min += need_time
    quota = int(need_time / 60)
    if int_min > 59:
        min_quota = int(int_min / 60)
        int_hour += min_quota
        int_min -= 60 * min_quota
    if int_hour >= 24:
        int_hour -= 24
    else:
        int_hour += quota

print(str(int_hour) + " " +str(int_min))