def pat(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        for k in range(i):
            print(chr(i + 65 - 1), end=' ')
        print()


pat(5)
