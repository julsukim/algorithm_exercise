import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
# 편의상, 첫 번째 메시지를 인덱스 1로 맞추기 위해 앞에 [0,0]을 넣을 수도 있지만,
# 여기서는 그대로 인덱스 0..K-1 사용.
messages = [input().split() for _ in range(K)]

# 사람 목록: A부터 N명. A는 항상 읽으므로 제거 대상에서 제외
people = [chr(c) for c in range(ord('A'), ord('A') + N)]
participants = set(people[1:])  # A 빼고 (people[0] = 'A')

# Q번 메시지의 R값 (문자열로 들어왔을 수 있으니 int 변환 유의)
#  - messages는 0-based 인덱스, Q는 1-based. => messages[Q-1]
R_Q = messages[Q-1][0]  # 문자열
sender_Q = messages[Q-1][1]

# [1] 만약 Q번 메시지의 R==0이면 => -1 출력 후 종료
if R_Q == '0':
    print(-1)
    sys.exit()

# [2] Q번 (인덱스 Q-1) ~ K-1까지: 메시지 송신자 제거
for i in range(Q-1, K):
    sender = messages[i][1]
    if sender in participants:
        participants.remove(sender)

# [3] Q-1부터 거꾸로 0까지:
#     Q번 메시지의 R값과 '같은' R이면 송신자 제거, 다른 값 만나면 break
for i in range(Q-2, -1, -1):
    if messages[i][0] == R_Q:
        sender = messages[i][1]
        if sender in participants:
            participants.remove(sender)
    else:
        break

# [4] 결과 출력
if len(participants) == 0:
    print(-1)
else:
    print(*sorted(participants))
