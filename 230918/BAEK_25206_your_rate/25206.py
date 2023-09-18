grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_score = 0.0
total_grade = 0.0
for _ in range(20):
    result = list(input().split())
    if result[2] == 'P':
        pass
    else:
        total_score += float(result[1])
        total_grade += float(result[1]) * grade[result[2]]

total_grade = total_grade / total_score
print(total_grade)
