import math


def distinction_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


number_length = int(input())
number = 2

if number_length != 1:
    number = number * (10 ** (number_length - 1))

is_right = True
false_set = set()
true_list = []
while number < (10 ** number_length):
    str_number = str(number)

    for i in range(len(str_number)):
        target = int(str_number[:i+1])

        if target in false_set:
            is_right = False
            break

        result = distinction_prime(target)

        if not result:
            is_right = False
            false_set.add(target)
            break

    if is_right:
        true_list.append(number)

    number += 1
    is_right = True

print(true_list)
