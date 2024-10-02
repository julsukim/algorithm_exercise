import time

# 큰 리스트 생성
large_list = ['apple'] * 100000

# join() 방식
start = time.time()
result_1 = "".join(large_list)
print(f"join: {time.time() - start} seconds")

# 반복문 방식
start = time.time()
result_2 = ""
for c in large_list:
    result_2 += c
print(f"for loop: {time.time() - start} seconds")
