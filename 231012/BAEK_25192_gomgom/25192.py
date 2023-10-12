import sys
input = sys.stdin.readline


N = int(input().rstrip())
count = 0
record_set = set()
for _ in range(N):
    record = input().rstrip()
    if record == 'ENTER':
        count += len(record_set)
        record_set = set()
    else:
        if record not in record_set:
            record_set.add(record)
else:
    count += len(record_set)
    record_set = set()
print(count)
