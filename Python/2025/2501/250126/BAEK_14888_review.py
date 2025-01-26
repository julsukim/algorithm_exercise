N = int(input())
sequence = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())

maximum = -10**10
minimum = 10**10


def c14(number, div):
    if number < 0:
        return -((-number) // div)
    return number // div


def recur(i, total, plus, minus, multi, divide):
    global maximum, minimum
    if i == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus > 0:
        recur(i+1, total+sequence[i], plus-1, minus, multi, divide)
    if minus > 0:
        recur(i+1, total-sequence[i], plus, minus-1, multi, divide)
    if multi > 0:
        recur(i+1, total*sequence[i], plus, minus, multi-1, divide)
    if divide > 0:
        recur(i+1, c14(total, sequence[i]), plus, minus, multi, divide-1)


recur(1, sequence[0], plus, minus, multi, divide)

print(maximum)
print(minimum)
