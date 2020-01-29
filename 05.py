def pat(n):
    spc = n - 1
    srt = 1
    for i in range(n):
        for j in range(spc):
            print("* ", end="")
        for j in range(srt):
            print("  ", end="")
        for j in range(spc):
            print("* ", end="")
        print()
        spc -= 1
        srt += 2

    spc = 1
    srt = 2 * (n - 1)
    for i in range(n - 1):
        for j in range(spc):
            print("* ", end="")
        for j in range(srt - 1):
            print("  ", end="")
        for j in range(spc):
            print("* ", end="")
        print()
        spc += 1
        srt -= 2


pat(5)
