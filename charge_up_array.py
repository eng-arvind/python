def solve (A,N):
    m = pow(10,9)+7
    ch= int(pow(2,N)//2)
    s=0
    for i in range(N):
        if A[i]>=ch:
            s+=A[i]
    return s%m

T = int(input())
for _ in range(T):
    N = int(input())
    A = map(int, input().split())

    out_ = solve(A,N)
    print (out_)

  
