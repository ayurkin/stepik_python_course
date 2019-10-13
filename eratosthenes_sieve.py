def eratosthenes_sieve(N):
    A = [True]*N
    b = []
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False

    for k in range(N):
        print(k, '-', "простое" if A[k] else "составное")

eratosthenes_sieve(222)