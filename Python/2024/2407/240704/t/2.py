from itertools import permutations

def generate_all_rotations(cube):
    # 가능한 모든 회전을 생성하는 헬퍼 함수
    def rotate(cube, rotations):
        new_cube = cube
        for axis, steps in rotations:
            if axis == 'x':
                new_cube = rotate_x(new_cube, steps)
            elif axis == 'y':
                new_cube = rotate_y(new_cube, steps)
            elif axis == 'z':
                new_cube = rotate_z(new_cube, steps)
        return new_cube

    # x축을 중심으로 회전
    def rotate_x(cube, steps):
        for _ in range(steps):
            cube = [cube[4], cube[0], cube[2], cube[3], cube[5], cube[1]]
        return cube

    # y축을 중심으로 회전
    def rotate_y(cube, steps):
        for _ in range(steps):
            cube = [cube[0], cube[3], cube[1], cube[4], cube[2], cube[5]]
        return cube

    # z축을 중심으로 회전
    def rotate_z(cube, steps):
        for _ in range(steps):
            cube = [cube[2], cube[1], cube[5], cube[3], cube[0], cube[4]]
        return cube

    rotations = set()
    axes = ['x', 'y', 'z']
    for perm in permutations(axes, 3):
        for steps in range(4):
            rotations.add(tuple(zip(perm, [steps, steps, steps])))

    all_rotations = set()
    for rotation in rotations:
        rotated_cube = rotate(cube, rotation)
        all_rotations.add(''.join(rotated_cube))

    return all_rotations

def compare_cubes(cube1, cube2):
    # 모든 회전 가능한 경우를 생성합니다.
    rotations1 = generate_all_rotations(list(cube1))
    rotations2 = generate_all_rotations(list(cube2))
    # 두 정육면체가 동일한지 비교합니다.
    return 1 if rotations1.intersection(rotations2) else 0

def compare_cubes_in_queries(queries):
    results = []
    for cube1, cube2 in queries:
        results.append(compare_cubes(cube1, cube2))
    return results

# 입력 예시
queries = [["YOWRGB", "WOYRBG"], ["YOWRGB", "WOYRGB"], ["BGORWY", "BGORWY"]]
# 결과 출력
result = compare_cubes_in_queries(queries)
print(result)  # 예상 출력: [1, 0, 1]
