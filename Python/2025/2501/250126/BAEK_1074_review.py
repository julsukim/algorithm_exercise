N, r, c = map(int, input().split())


def z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** n // 2
    ns = half * half

    # top left
    if r < half and c < half:
        return z(n - 1, r, c)
    # top right
    elif r < half and c >= half:
        return ns + z(n - 1, r, c - half)
    # bottom left
    elif r >= half and c < half:
        return ns * 2 + z(n - 1, r - half, c)
    # bottom right
    elif r >= half and c >= half:
        return ns * 3 + z(n - 1, r - half, c - half)


print(z(N, r, c))
