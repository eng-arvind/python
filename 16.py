def pat(n):
    for i in range(n):
        k = 65
        for j in range(n-1-i):
            print("  ", end="")
        srt = 2 * i + 1
        for j in range(srt):
            print(chr(k), end=" ")
            k = k + 1 if j < i else k - 1
        print()
    for i in range(n-2, -1, -1):
        k = 65
        for j in range(n-1-i):
            print("  ", end="")
        srt = 2 * i + 1
        for j in range(srt):
            print(chr(k), end=" ")
            k = k + 1 if j < i else k - 1
        print()


pat(5)
