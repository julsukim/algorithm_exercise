import sys
sys.stdin = open('simple_input.txt')


def hex_to_bin(arr):
    binary = ''
    bin_arr = []
    for hex in arr:
        if hex:     # 빈 문자열이 존재하기 때문에 값이 있는 것만 2진수로 변환
            for h in hex:   # 16진수 문자열 1개씩 4개의 bit로 구성하여 저장
                binary += f'{int(h, base=16):04b}'
            bin_arr.append(binary)
    return bin_arr


def get_width(arr):
    width_list = []
    for row in range(len(arr)):
        count = 0
        before = '0'  # 현재 값을 저장 (다음 값과 비교하기 위해)
        change = 0  # 숫자가 0 -> 1, 1 -> 0으로 몇 번 바뀌었는지 확인용 변수
        for col in range(len(arr[row])-1, -1, -1):
            if before != arr[row][col]:
                # 숫자가 전환되는 횟수
                if change == 4:
                    break
                change += 1
                before = arr[row][col]
            if arr[row][col] == '1':
                # 왼쪽에서 처음 만났을 경우 (시작점)
                if count == 0:
                    end_point = col
                count += 1
            if count and arr[row][col] == '0':
                count += 1

        if change == 4:
            width_list.append((count // 7, end_point))

    return width_list


def scanner(bin_arr, width_list):
    pw_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    for row in range(len(bin_arr)):
        while bin_arr[row]:
            width, end_point = width_list[row]  # 코드의 배수 정보, 끝점
            # 코드 자르기
            binary = bin_arr[row][end_point - 56*width + 1: end_point+1:width]

            # 자른 코드를 검증하기
            pw_list = []
            for i in range(8):  # 8자리의 암호이기에 8번 반복
                bit_number = binary[i*7: (i+1)*7]
                pw_list.append(pw_dict[bit_number]) # 암호를 담자

            # 담은 암호를 검증
            even_sum = sum(pw_list[1::2])
            odd_sum = sum(pw_list[::2])
            if (odd_sum * 3 + even_sum) % 10 == 0:
                print(True)
            else:
                print(False)

            bin_arr[row] = bin_arr[:end_point - 56 * width +1]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 세로, M: 가로
    arr = list(set([input().rstrip('0') for _ in range(N)]))
    # 16진수를 2진수로 변환 완료!
    bin_arr = hex_to_bin(arr)
    # 과연 몇 배수로 이루어져 있는지 확인!!
    # 마지막 숫자 정보를 읽어서 7의 몇 배수인지 확인, 마지막 지점 정보도 같이 가져오자
    width_list = get_width(bin_arr) # 배수 정보와 마지막 지점이 리스트로 전달
    # 실제로 데이터를 잘라다가 확인하는 함수
    scanner(bin_arr, width_list)