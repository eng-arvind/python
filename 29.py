def pat(n):
    for i in range(n // 2 + 1):
        for j in range(n):
            if i + j == n // 2 or i - j == -n // 2 + 1 or j - i == -n // 2 + 1 or i + j == n + (n // 2 - 1):
                print(i + 1, end='')
            else:
                print(' ', end='')
        print()


pat(5)
