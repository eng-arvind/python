def pat(n):
    for i in range(n, 0, -1):
        c = i
        for j in range(n - i):
            print(' ', end='')
        for k in range(i):
            print(c, end=' ')
            c -= 1
        print()


pat(5)
