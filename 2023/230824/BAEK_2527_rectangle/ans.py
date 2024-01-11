import sys
sys.stdin = open('input.txt')

T = 4
for tc in range(1, T+1):
    ans = 0
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        ans = "d"
    else:
        if (x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2) or (x2 == p1 and q2 == y1) or (x2 == p1 and y2 == q1):
            ans = "c"
        else:
            if x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
                ans = "b"
            else:
                ans = "a"
    print(ans)