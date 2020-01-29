def pat(n):
    k = 65
    for i in range(n):
        for j in range(n):
            print(chr(k), end="") if i+j <= n-1 else print("", end="")
        k += 1
        print()


pat(5)
