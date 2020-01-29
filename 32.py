def pat(n):
    half = n // 2
    for i in range(n // 2 + 1):
        for j in range(n):
            if i + j == n // 2 or i - j == -n // 2 + 1 or j - i == -n // 2 + 1 or i + j == n + (n // 2 - 1):
                print(chr(half + 65), end='')
            else:
                print(' ', end='')
        half -= 1
        print()


pat(5)
