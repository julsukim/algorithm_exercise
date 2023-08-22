import sys
sys.stdin = open('finput.txt')

T = 4
for tc in range(T):
    arr = list(map(int, input().split()))

    result = 'd'

    vers1 = [(arr[0], arr[1]), (arr[0], arr[3]), (arr[2], arr[1]), (arr[2], arr[3])]
    vers2 = [(arr[4], arr[5]), (arr[4], arr[7]), (arr[6], arr[5]), (arr[6], arr[7])]

    for i in vers1:
        for j in vers2:
            if i == j:
                result = 'c'

    if arr[0] == arr[6] or arr[2] == arr[4]:
        result = 'b'
    elif arr[1] == arr[7] or arr[3] == arr[5]:
        result = 'b'

    for x, y in vers1:
        if arr[4] < x < arr[6] and arr[5] < y < arr[7]:
            result = 'a'

    for x, y in vers2:
        if arr[0] < x < arr[2] and arr[1] < y < arr[3]:
            result = 'a'

    if (arr[4] < arr[0] < arr[6] and arr[4] < arr[2] < arr[6]) and (
            arr[1] < arr[5] < arr[3] and arr[1] < arr[7] < arr[3]):
        result = 'a'
    elif (arr[0] < arr[4] < arr[2] and arr[0] < arr[6] < arr[2]) and (
            arr[5] < arr[1] < arr[7] and arr[5] < arr[3] < arr[7]):
        result = 'a'

    print(result)