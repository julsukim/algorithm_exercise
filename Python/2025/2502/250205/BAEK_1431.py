import sys
input = sys.stdin.readline

N = int(input())
serial_numbers = [input().rstrip() for _ in range(N)]

serial_numbers.sort(key=lambda x: (len(x), sum([int(i) for i in x if i.isdigit()]), x))
print('\n'.join(serial_numbers))
