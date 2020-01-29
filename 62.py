def pat(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if i + j <= n:
                print('*', end='')
            else:
                print(' ', end='')
        for k in range(n):
            if k < i:
                print('*', end='')
        print()


pat(5)
