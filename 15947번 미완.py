song = 'baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan'
song_list = song.split()
n = int(input())
cnt = 0
tururu = 'tururu'
turu = 'turu'
if n > 14:
    cnt = n // 14
    if cnt >= 3:
        if tururu in song_list:
            print('tu+ru'+ '*' + str(cnt+2))
    elif cnt >= 4:
        if turu in song_list:
            print('tu+ru'+ '*' + str(cnt-2))     
    while True:
        if cnt == 0:
            break
        song_list[2] += 'ru'
        song_list[3] += 'ru'
        song_list[6] += 'ru'
        song_list[7] += 'ru'
        song_list[10] += 'ru'
        song_list[11] += 'ru'
        cnt -= 1    
print(song_list[(n-1) % 14])   