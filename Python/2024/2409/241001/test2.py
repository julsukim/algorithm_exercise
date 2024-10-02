import time

# 테스트 문자열과 부분 문자열
test_string = "abcde" * 100000
sub_string = "bc"

# str.count() 방식
start = time.time()
result_1 = test_string.count(sub_string)
print(result_1)
print(f"str.count(): {time.time() - start} seconds")

# 반복문 방식
def custom_count(string, sub):
    count = 0
    sub_len = len(sub)
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == sub:
            count += 1
    return count

start = time.time()
result_2 = custom_count(test_string, sub_string)
print(result_2)
print(f"custom_count(): {time.time() - start} seconds")
