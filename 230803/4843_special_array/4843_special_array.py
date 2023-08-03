import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    special_list = []
    maximum = 0
    minimum = 0
    for num in range(10):
        for i in range(0, len(num_list)):
            if maximum < num_list[i]:
                maximum = i
        for j in range(0, len(num_list)):
            if minimum > num_list[j]:
                minimum = j
        special_list.append(num_list.pop(i))
        special_list.append(num_list.pop(j))



    print(special_list)