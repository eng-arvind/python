def pat(n):
    m1 = n
    m2 = 0
    for i in range(n):
        if i % 2 == 0:
            m1 -= 2
            m2 += 2
        for j in range(m1):
            print(' ', end='')
        for j in range(m2):
            print('*', end='')
        print()


pat(6)
