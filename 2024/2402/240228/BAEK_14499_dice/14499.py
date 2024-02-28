# 14499 주사위 굴리기
# 동 1, 서 2, 북 3, 남 4
# 상단에 쓰여있는 값 출력
# 지도 바깥으로 이동 -> 명령 무시, 출력 X
N, M, x, y, K = map(int, input().split())
zido = []
for i in range(N):
    zido.append(list(map(int, input().split())))
order = list(map(int, input().split()))

print(zido, order)
hori = [0] * 4
vert = [0] * 4
print(hori, vert)
top = 1
bottom = 3
