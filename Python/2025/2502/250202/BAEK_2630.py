import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0


def cut(n, si, ei, sj, ej):
    global white, blue

    current = sum([sum(line[sj:ej]) for line in paper[si:ei]])
    if current == 0:
        white += 1
        return
    elif current == n ** 2:
        blue += 1
        return

    half = n//2
    cut(half, si, ei-half, sj, ej-half)
    cut(half, si, ei-half, sj+half, ej)
    cut(half, si+half, ei, sj, ej-half)
    cut(half, si+half, ei, sj+half, ej)


cut(N, 0, N, 0, N)

print(white)
print(blue)
