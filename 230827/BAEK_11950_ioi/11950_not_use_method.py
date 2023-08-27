'''
하얀색 , 파란색, 빨간색이 적어도 한줄 들어가기만 하면 되는 경우이다.
행 기준으로 하얀색의 기준은 ~i 까지, 파란색은 i+1 ~ j , 빨간색은 j+1~N 이다.
'''


N, M = map(int,input().split())
arr = [input() for _ in range(N)]

max_v = 0
for i in range(N-2):   # 하얀색여야하는는  행범위 설정 다른 파랑, 빨강이 적어도 1줄은 들어가야 하니 범위는 N-2로 한다.
    for j in range(i+1, N-1):  # 파랑색이여야 하는 범위 설정, 빨강이 적어도 1줄은 들어가야하니 N-1 이다.
        cnt = 0        # 임시 변수
        for s in range(i+1):  # 하얀색이여야 하는행
            for k in range(M):
                if arr[s][k] == 'W': # 하얀색이라면
                    cnt += 1         # 플러스 1해라
        for s in range(i+1, j+1):  # 파란색이여야 하는행
            for k in range(M):
                if arr[s][k] == 'B': # 파란색이면
                    cnt += 1         # 플러스 1해라
        for s in range(j+1, N):  # 빨간색이여야 하는 행
            for k in range(M):
                if arr[s][k] == 'R': # 빨강이면
                    cnt += 1         # 플러스 1해라
        if cnt > max_v:  #맥스값 갱신
            max_v = cnt
print(N*M -max_v)
'''
mx 의 의미는 하얀색이 있어야 하는행, 파란색이 있어야 하는 행, 빨간색이 있어야할 행에 수정할 필요가 없는 영역의 개수 이다.
다시 이야기하면, 하얀색 행에 하얀색은 수정할 필요가 없기 때문에, 하얀색 개수를 카운팅 한것이고, 나머지 색도 마찬가지다.
수정해야할 최소 개수를 구하라 했으니, 전체 영역의 개수 - mx를 하면 답이 나온다. '''