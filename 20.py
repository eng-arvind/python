def pat(n):
    for i in range(n, 0, -1):
        c = i
        for j in range(n - i):
            print(' ', end='')
        for k in range(i):
            print(chr(c + 65 - 1), end=' ')
            c -= 1
        print()


pat(5)
