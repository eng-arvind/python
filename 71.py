def pat(n):
    m1 = n - n // 2 + 1
    m2 = 0
    for i in range(n):
        if i % 2 == 0:
            m1 -= 1
            m2 += 1
        for j in range(m1):
            print(' ', end='')
        for j in range(m2):
            print('*', end='')
        for j in range(m2-1):
            print('*', end='')
        print()


pat(6)
