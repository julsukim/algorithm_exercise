# 인접 행렬
# 장점 : 구현이 쉽다
# 단점 : 메모리 낭비 (0로 표시를 하기 때문에)
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

# 인접 리스트
# 갈 수 있는 지점만 저장한다
# 주의사항
#   각 노드마다 갈 수 있는 지점의 개수가 다름
#   -> range 쓸 때 index 조심
# 메모리가 인접 행렬에 비해 훨씬 효율적이다.
# 딕셔너리로도 구현이 가능 (ex. 요소명이 정수가 아닐 때)
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]

# DFS
# stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]
    while stack:
        now = stack.pop()

        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 작은 번호부터 조회
        for next in range(len(graph[now])-1, -1, -1):
            # 방문한 지점이라면 stack에 추가하지 않음
            if graph[now][next] in visited:
                continue

            stack.append(graph[now][next])
    # 출력을 위한 반환
    return visited


print(*dfs_stack(0))


# 재귀
# MAP 크기(길이)를 알 때,
# append 형식대신 아래와 같이 사용하면 더 빠름
visited = [0] * 5
path = []   # 방문 순서 기록


def dfs(now):
    visited[now] = 1
    # path.append(now)
    print(now, end=' ')

    # 인접합 노드들을 방문
    for next in range(len(graph[now])):
        if visited[graph[now][next]]:
            continue

        dfs(graph[now][next])


dfs(0)