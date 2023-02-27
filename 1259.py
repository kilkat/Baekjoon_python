while True:
    num = input()
    if num == '0':
        break

    reverse_string = num[::-1]
    print("yes" if (num == reverse_string) else "no")