import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
messages = [input().split() for _ in range(K)]
# alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabets = [chr(x) for x in range(ord('A'), ord('Z')+1)]
participants = set(alphabets[:N])
participants.remove(alphabets[0])

if messages[Q-1][0] == 0:
    print(-1)
    sys.exit(0)

for i in range(Q-1, K):
    if messages[i][1] in participants:
        participants.remove(messages[i][1])

    if messages[i][0] == 0:
        participants.clear()
        break

unread_Q = messages[Q-1][0]
for j in range(Q-1, -1, -1):
    if messages[j][0] == unread_Q:
        if messages[j][1] in participants:
            participants.remove(messages[j][1])
    else:
        break

if len(participants) == 0:
    print(-1)
else:
    print(*sorted(list(participants)))
