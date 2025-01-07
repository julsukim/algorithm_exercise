shorten = input()


def expand_ipv6(address: str) -> str:
    # 1. :: 처리
    if "::" in address:
        left_side, right_side = address.split("::", 1)

        # 왼쪽 / 오른쪽 그룹 분리 (빈 문자열인 경우 주의)
        left_groups = left_side.split(":") if left_side else []
        right_groups = right_side.split(":") if right_side else []

        # 총 8개 그룹 중, 이미 있는 그룹만큼 제외한 수
        missing_count = 8 - (len(left_groups) + len(right_groups))

        # :: 으로 생략된 그룹을 0으로 채움
        middle_groups = ["0"] * missing_count

        groups = left_groups + middle_groups + right_groups
    else:
        # :: 가 없으면, : 로만 나눈 그룹이 8개여야 함
        groups = address.split(":")

    # 2. 각 그룹을 4자리 16진수로 확장
    # str.zfill(width) : width 만큼의 길이로 나머지 부분을 '0'으로 채움.
    # s = '42' => s.zfill(5) => '00042'
    expanded_groups = [g.zfill(4) for g in groups]

    # 3. 8개 그룹을 콜론으로 이어붙여 최종 결과 생성
    return ":".join(expanded_groups)


print(expand_ipv6(shorten))

# print(shorten)
#
# cnt = 0
# v1 = ''
# prev = ''
# tmp = ''
# for ad in shorten:
#     if ad == ':':
#         if tmp != '':
#             v1 += '0' * (4 - len(tmp)) + tmp + ':'
#             cnt += 1
#             tmp = ''
#         elif tmp == '' and prev == ':':
#             v1 += ':' * 2
#         prev = ':'
#     else:
#         tmp += ad
#         prev = ad
# else:
#     if tmp != '':
#         v1 += '0' * (4 - len(tmp)) + tmp
#         cnt += 1
#
# if cnt == 8:
#     print(v1)
# else:
