def pat(n):
    for i in range(n):
        for j in range(n-1-i):
            print("  ", end="")
        srt = 2 * i + 1
        k = 64 + srt
        for j in range(srt):
            print(chr(k), end=" ")
            k -= 1
        print()
    for i in range(n-2, -1, -1):
        for j in range(n-1-i):
            print("  ", end="")
        srt = 2 * i + 1
        k = 64 + srt
        for j in range(srt):
            print(chr(k), end=" ")
            k -= 1
        print()


pat(5)
