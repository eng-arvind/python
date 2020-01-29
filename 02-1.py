def pat(n):
    for i in range(n):
        half = n // 2
        for j in range(n // 2, n + 1):
            if i + j < n // 2 or i - j <= -n // 2 or j - i <= -n // 2 or i + j > n + (n // 2 - 1):
                print(' ', end='')
            else:
                print(half, end='')
            half -= 1
        print()


pat(5)
