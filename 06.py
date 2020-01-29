def pat(n):
    for i in range(n):
        for j in range(n-1-i):
            print("  ", end="")
        srt = 2 * i + 1
        for j in range(srt):
            print("  ", end="") if 0 < j < srt - 1 else print("* ", end="")
        print()
    for i in range(n-2, -1, -1):
        for j in range(n-1-i):
            print("  ", end="")
        srt = 2 * i + 1
        for j in range(srt):
            print("  ", end="") if 0 < j < srt - 1 else print("* ", end="")
        print()


pat(5)
