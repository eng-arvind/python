def pat(n):
    m = n
    m = m // 2
    m += 1
    for i in range(m):
        for j in range(m - i - 1):
            print(' ', end='')
        for k in range(i + 1):
            print('* ', end='')
        print()
    for i in range(m - 2, -1, -1):
        for j in range(m - i - 1):
            print(' ', end='')
        for k in range(i + 1):
            print('* ', end='')
        print()


pat(5)
