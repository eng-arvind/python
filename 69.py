def pat(n):
    m = n - n // 2 + 1
    for i in range(n):
        if i % 2 == 0:
            m -= 1
        for j in range(m):
            print('*', end='')
        print()


pat(6)
