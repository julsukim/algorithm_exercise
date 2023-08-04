# def select(arr, k):
#     for i in range(0, k):
#         min_idx = i
#         max_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#             if arr[max_idx] < arr[j]:
#                 max_idx = j
#         return min_idx, max_idx
#
num_list = [1, 2, 3, 4, 5]
# print(select(num_list, 4))

def special_array(arr):
    for i in range(0, len(arr)):
        min_idx = i
        max_idx = i
        if i % 2 != 1:
            for j in range(i+1, len(arr)):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            for k in range(i+1, len(arr)):
                if arr[min_idx] > arr[k]:
                    min_idx = k
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(special_array(num_list))