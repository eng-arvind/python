def pat(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        for k in range(i):
            print(i, end=' ')
        print()


pat(5)
