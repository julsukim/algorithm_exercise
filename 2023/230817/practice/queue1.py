def enQ(data):
    global rear
    # if rear==Qsize-1:    # 가득 차면
    #     print('Q is Full')
    # else:
    rear += 1
    Q[rear] = data


def deQ():
    global front
    # if front==rear:    # 비어있으면
    #     print('Q is Empty')
    #     return -1
    # else:
    front += 1
    return Q[front]


Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1

enQ('A')
enQ('B')
enQ('C')
# # enQ('D')
# print(deQ())
# print(deQ())
# print(deQ())
# # print(deQ())

while front != rear:
    front += 1
    print(Q[front])