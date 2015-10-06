def euclid(n, m):
    if max(n, m) % min(n, m) == 0:
        return min(n, m)
    return euclid(min(n, m), max(n, m) % min(n, m))


def rpfilter(a, *args):
    rp_numbers = []
    for number in args:
        if euclid(number, a) == 1:
            rp_numbers.append(number)
    if len(rp_numbers) == 0:
        rp_numbers.append(None)
    return rp_numbers


print(" ".join((str(x) for x in rpfilter(*(int(x) for x in input().split())))))
