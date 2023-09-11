student_list = [0] * 31
for _ in range(28):
    stu_idx = int(input())
    student_list[stu_idx] = 1
for i in range(1, len(student_list)):
    if student_list[i] != 1:
        print(i)
