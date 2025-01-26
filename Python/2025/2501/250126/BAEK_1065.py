N = int(input())

# 양의 정수 X의 각 자리가 등차수열을 이루면 그 수는 한수
# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력
# 한수 : 1, 11, 15, 19, ... 100 미만의 수는 모두 한수

if N < 100:
    print(N)
else:
    result = 99
    for i in range(100, N+1):
        number = str(i)
        diff = int(number[0]) - int(number[1])
        flag = True
        for j in range(1, len(number) - 1):
            tmp = int(number[j]) - int(number[j+1])
            if tmp != diff:
                flag = False
                break
        if flag:
            result += 1

    print(result)


def count_hansu(N):
    # 1) N < 100인 경우
    if N < 100:
        return N

    # 1~99까지는 전부 한수
    count = 99

    # N이 1000이면, 예외적으로 따로 처리(1000은 한수가 아님)
    if N == 1000:
        return 144  # 1~999까지의 한수 개수: 99 + 3자리 한수(45개) = 144

    # 2) 100 <= N < 1000인 경우:
    #    A(맨 앞 자리) = 1~9, 차이 d = -4..4를 통해 3자리 한수를 전부 생성
    for A in range(1, 10):  # 1~9
        for d in range(-4, 5):  # -4..4
            B = A + d
            C = A + 2 * d
            # 세 자리 모두 0~9 범위 내인지 확인
            if 0 <= B <= 9 and 0 <= C <= 9:
                num = 100 * A + 10 * B + C
                # N 이하인지 확인
                if num <= N:
                    count += 1

    return count
