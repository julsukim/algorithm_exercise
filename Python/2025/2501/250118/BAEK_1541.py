# # 괄호를 쳐서 식의 값을 최소로 만들기
# equation = input()
# split_equation = []
# tmp = ''
# for c in equation:
#     if c == '+' or c == '-':
#         if tmp != '':
#             split_equation.append(int(tmp))
#             tmp = ''
#         split_equation.append(c)
#     else:
#         tmp += c
# else:
#     if tmp != '':
#         split_equation.append(int(tmp))
#         tmp = ''
#
# total = split_equation[0]
# tmp = 0
# on = False
#
# for i in range(1, len(split_equation)):
#     if on:
#         if split_equation[i] == '-':
#             total -= tmp
#             tmp = 0
#         elif split_equation[i] != '+':
#             tmp += split_equation[i]
#     else:
#         if split_equation[i] == '-':
#             on = True
#             continue
#         elif split_equation[i] != '+':
#             total += split_equation[i]
# else:
#     total -= tmp
#
# print(total)


expression = input().strip()
split_by_minus = expression.split('-')
print(split_by_minus)

# 첫 덩어리는 전부 더함
result = sum(map(int, split_by_minus[0].split('+')))
print(result)

# 나머지 덩어리는 더한 뒤 한 번에 빼기
for part in split_by_minus[1:]:
    print(part)
    result -= sum(map(int, part.split('+')))
    print(result)

print(result)
