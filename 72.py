def pat(n):
    for i in range(n):
        for j in range(n):
            print('*', end='') if i == 0 or j == 0 or i == n-1 or j == n-1 else print(' ', end='')
        print()


pat(6)
