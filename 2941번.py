cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input() #ljes=njak
for i in cro_list:
    if i in cro_list:
        a = a.replace(i, '0')
print(len(a))