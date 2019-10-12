def combination(n, k):
    if n == k and n > 0 or (n > 0 and k == 0):
        return 1
    elif n == 0 or k > n:
        return 0
    else:
        return combination(n - 1, k) + combination(n - 1, k - 1)


n, k = map(int, input().split())
print(combination(n, k))

