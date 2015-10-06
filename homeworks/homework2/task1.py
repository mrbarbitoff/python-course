def combinations(n, k):
    if k > n:
        return 0
    if k == n or k == 0:
        return 1
    return combinations(n - 1, k - 1) + combinations(n - 1, k)


print(combinations(*(int(x) for x in input().split())))
