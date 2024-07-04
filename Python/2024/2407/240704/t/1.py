# 1 ~ N
# pass X, + salary
# before close holiday
# 1 max
N = int(input())
X = int(input())
salary = int(input())
# manual
holidays = [[4, 6]]
result = 0

def solution():
    pay_days = []
    day = X
    while day <= N:
        pay_days.append(day)
        day += X

    actual_pay_days = []
    holidays_idx = 0

    for pay_day in pay_days:

        while holidays_idx < len(holidays) and holidays[holidays_idx][1] < pay_day:
            holidays_idx += 1
