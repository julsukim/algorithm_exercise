# 내가 푼 풀이

"""
N = int(input())

count = 0

bosu = ~N + 1
hello = bin(~(bosu ^ N))[2:].zfill(32)
for s in hello:
    if s == "0":
        count += 1
print(count)
"""

# GPT 참고

N = int(input())

bosu = ~N + 1
N_32bit = N & 0xFFFFFFFF
bosu_32bit = bosu & 0xFFFFFFFF

count = bin(N_32bit ^ bosu_32bit).count('1')
print(count)

"""
0xFFFFFFFF는 16진수로 표현된 숫자로, 32비트의 모든 비트가 1인 숫자를 의미합니다.
16진수 F는 10진수로 15이고, 이진수로는 1111입니다.
어떤 값을 32비트로 제한하고 싶다면, 해당 값과 0xFFFFFFFF를 AND 연산(&)하면 됩니다.
이렇게 하면 상위 32비트 이외의 값들은 모두 0으로 만들어져 실제로 32비트만 남게 됩니다.
"""
