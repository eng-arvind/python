def pat(n):
    m = n + 2
    for i in range(n):
        if i % 2 == 0:
            m -= 2
        for j in range(m):
            print('*', end='')
        print()


pat(6)
