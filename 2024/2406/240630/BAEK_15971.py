from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
graph = list([] for i in range(N+1))

for _ in range(N-1):
    n1, n2, l = map(int, input().split())
    if (n1 == A or n2 == A) and (n1 == B or n2 == B):
        print(0)
        sys.exit(0)
    graph[n1].append([n2, l])
    graph[n2].append([n1, l])

INF = float('inf')
dist = [INF]*(N+1)
prev = [-1]*(N+1)
pq = []
heappush(pq, (0, A))
dist[A] = 0
prev[A] = 0

while pq:
    d, n = heappop(pq)

    if dist[n] < d:
        continue

    for next in graph[n]:
        next_node = next[0]
        next_dist = next[1]

        new_dist = d + next_dist

        if dist[next_node] <= new_dist:
            continue

        dist[next_node] = new_dist
        prev[next_node] = n
        heappush(pq, (new_dist, next_node))

path = []
max_edge = 0
current_node = B

while current_node != A:
    path.append(current_node)
    current_node = prev[current_node]
path.append(A)

for i in range(1, len(path)):
    u, v = path[i-1], path[i]
    for next_node, next_dist in graph[u]:
        if next_node == v:
            max_edge = max(max_edge, next_dist)
            break

print(dist[B] - max_edge)


# from sys import stdin
# from collections import deque
#
# input = stdin.readline
# n,start,end = map(int, input().split())
# adj_list = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a,b,c = map(int, input().split())
#     adj_list[a].append((b,c))
#     adj_list[b].append((a,c))
#
# def solv():
#     visited = [False]*(n+1)
#     q = deque([(start,0,0)])
#     visited[start] = True
#     while q:
#         now,total,max_cost = q.pop()
#         if now == end:
#             print(total-max_cost)
#             return
#         for nxt,cost in adj_list[now]:
#             if not visited[nxt]:
#                 visited[nxt] = True
#                 q.appendleft((nxt,total+cost,max(max_cost,cost)))
# solv()
