def pat(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()


pat(5)
