def pat(n):
    n = n // 2
    n += 1
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(i + 1):
            print(i + 1, end=' ')
        print()
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(i + 1):
            print(i + 1, end=' ')
        print()


pat(5)
