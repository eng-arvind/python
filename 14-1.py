def pat(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(i + 1):
            print(chr(i + 65), end=' ')
        print()


pat(5)
