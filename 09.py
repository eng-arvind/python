def pat(n):
    k = 1
    for i in range(n):
        for j in range(i + 1):
            print(k, end=" ")
            k = k + 1 if k < 9 else 1
        print()


pat(5)