import sys
sys.stdin = open('input.txt')

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    vert1 = [(x1, y1), (x1, q1), (p1, y1), (p1, q1)]
    vert2 = [(x2, y2), (x2, q2), (p2, y2), (p2, q2)]

    result = 'a'

    if (x1 < x2 and p1 < x2) or (x1 > p2 and p1 > p2):
        result = 'd'
    elif (y1 < y2 and q1 < y2) or (y1 > q2 and q1 > q2):
        result = 'd'

    for v1 in vert1:
        for v2 in vert2:
            if v1 == v2:
                result = 'c'

    if x1 == x2 or x1 == p2 or p1 == x2 or p1 == p2:
        if (y2 < y1 < q2) or (y2 < q1 < q2):
            result = 'b'
    if y1 == y2 or y1 == q2 or q1 == y2 or q1 == q2:
        if (x2 < x1 < p2) or (x2 < p1 < p2):
            result = 'b'

    for x, y in vert1:
        if (x2 < x < p2) and (y2 < y < q2):
            result = 'a'
    for x, y in vert2:
        if (x1 < x < p1) and (y1 < y < q1):
            result = 'a'

    # if ((x2 <= x1 <= p2) and (x2 <= p1 <= p2)) and ((y1 <= y2 <= q1) and (y1 <= q2 <= q1)):
    #     result = 'a'
    # if ((x1 <= x2 <= p1) and (x1 <= p2 <= p1)) and ((y2 <= y1 <= q2) and (y2 <= q1 <= q2)):
    #     result = 'a'

    print(result)