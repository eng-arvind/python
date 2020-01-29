def pat(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()


pat(5)
