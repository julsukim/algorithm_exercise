from collections import deque

N = int(input())
R = int(input())
recommendations = list(map(int, input().split()))

frame = deque()
counter = [0] * 101
for i in range(R):
    if len(frame) < N and recommendations[i] not in frame:
        frame.append(recommendations[i])
        counter[recommendations[i]] += 1
    elif len(frame) == N and recommendations[i] not in frame:
        remove = 0
        min_value = 1001
        for p in range(len(frame)):
            if counter[frame[p]] < min_value:
                remove = frame[p]
                min_value = counter[frame[p]]
        counter[remove] = 0
        frame.remove(remove)
        frame.append(recommendations[i])
        counter[recommendations[i]] += 1
    elif recommendations[i] in frame:
        counter[recommendations[i]] += 1

result = sorted(list(frame))
print(*result)
