# import matplotlib.pyplot as plt
#
# # 첫 번째 선분의 좌표
# points1 = [(1, 2), (5, 5), (7, 3)]
# x1, y1 = zip(*points1)
#
# # 두 번째 선분의 좌표
# points2 = [(1, 1), (7, 3), (5, 5)]
# x2, y2 = zip(*points2)
#
# # 그래프 그리기
# plt.plot(x1, y1, marker='o', linestyle='-', color='b', label='Line 1')  # 첫 번째 선
# plt.plot(x2, y2, marker='s', linestyle='--', color='r', label='Line 2') # 두 번째 선
#
# # 그래프 스타일 설정
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Two Line Segments')
#
# # 범례 추가
# plt.legend()
#
# # 격자 추가
# plt.grid(True)
#
# # 그래프 표시
# plt.show()

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ccw = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

if ccw < 0:
    print(-1)
elif ccw == 0:
    print(0)
elif ccw > 0:
    print(1)
