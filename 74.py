def pat(n):
    for i in range(n):
        for j in range(i):
            print('*', end='') if j == 0 or i == n-1 else print(' ', end='')
        print("*")


pat(6)
