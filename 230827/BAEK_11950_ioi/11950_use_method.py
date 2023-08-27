'''
하얀색 , 파란색, 빨간색이 적어도 한줄 들어가기만 하면 되는 경우이다.
행 기준으로 하얀색의 기준은 ~i 까지, 파란색은 i+1 ~ j , 빨간색은 j+1~N 이다.
'''


N, M = map(int,input().split())
arr = [input() for _ in range(N)]

max_v = 0
for i in range(N-2):  # 흰색 영역 인덱스 설정
    for j in range(i+1, N-1):  # 파랑색 영역 인덱스 설정 그리고 나머지는 빨강영역이다.
        cnt = 0
        for s in range(i+1):           #하얀 영역
            cnt += arr[s].count('W') # W의 개수를 세라
        for s in range(i+1, j+1):      # 파란 영역
            cnt += arr[s].count('B') # B의 개수를 세라
        for s in range(j+1, N):        # 빨간 영역
            cnt += arr[s].count('R') # R의 개수를 세라
        max_v = max(max_v, cnt)

print(N*M -max_v)

'''
mx 의 의미는 하얀색이 있어야 하는행, 파란색이 있어야 하는 행, 빨간색이 있어야할 행에 수정할 필요가 없는 영역의 개수 이다.
다시 이야기하면, 하얀색 행에 하얀색은 수정할 필요가 없기 때문에, 하얀색 개수를 카운팅 한것이고, 나머지 색도 마찬가지다.
수정해야할 최소 개수를 구하라 했으니, 전체 영역의 개수 - mx를 하면 답이 나온다. '''