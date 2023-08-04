'''
삼성시의 버스 노선

삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
Bi이하인 모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001 # 1-5000번 정류장을 지나는 노선 수
    for _ in range(N): # N개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1 # 현재 노선이 i번 정류장 정차

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(bus_stop)
    print(f'#{tc}', end= ' ')
    for x in bus_stop:
        print(cnt[x], end = ' ')
    print()