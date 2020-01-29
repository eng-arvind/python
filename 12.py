def pat(n):
    for i in range(n):
        k = 65
        for j in range(n - 1 - i):
            print("  ", end="")
        for j in range(2 * i + 1):
            print(chr(k), end=" ")
            k += 1
        print()


pat(5)
