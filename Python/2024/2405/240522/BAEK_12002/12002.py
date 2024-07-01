import itertools

n = int(input())
point = []  # (x, y)
x_point = []  # (x, point번호)
y_point = []  # (y, point번호)
result = float('inf')

for i in range(n):
    x, y = map(int, input().split())
    point_num = len(point)
    x_point.append((x, point_num))
    y_point.append((y, point_num))
    point.append((x, y))

x_point.sort()  # x좌표 기준으로 정렬
y_point.sort()  # y좌표 기준으로 정렬

# 소들 중 3개를 제거해서 직사각형을 작게 만들어야 하므로, 끝에 있는 점들중 3개를 고른다
# x좌표 기준으로 제일 작은것 3개, 제일 큰것 3개,
# y좌표 기준으로 제일 작은것 3개, 제일 큰것 3개,
# 후보중 3개를 뽑는다
temp = []  # 삭제할 후보

for i in range(3):
    temp.append(x_point[i][1])
    temp.append(y_point[i][1])
    temp.append(x_point[n - 1 - i][1])
    temp.append(y_point[n - 1 - i][1])

# 중복된 후보 제거
temp = list(set(temp))

for perm in itertools.combinations(temp, 3):
    remove_check = [0] * len(point)  # 삭제될 포인트 번호 체크
    for i in perm:
        remove_check[i] = 1

    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')
    for i in range(len(point)):
        if remove_check[i] == 1:
            continue

        x_min = min(x_min, point[i][0])
        x_max = max(x_max, point[i][0])
        y_min = min(y_min, point[i][1])
        y_max = max(y_max, point[i][1])

    len1 = x_max - x_min
    len2 = y_max - y_min
    result = min(result, len1 * len2)

print(result)
