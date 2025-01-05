import sys
input = sys.stdin.readline

N = int(input())
shortcut = set()
for _ in range(N):
    func = input().rstrip().split(' ')
    result = ''
    is_first = False
    set_coord = -1
    # 단어의 첫 글자로 단축키 설정 가능한지 확인
    for i in range(len(func)):
        char = func[i][0]
        if char.lower() in shortcut:
            continue
        else:
            set_coord = i
            is_first = True
            break

    is_set = False
    # 단어 조합하기
    for i in range(len(func)):
        # 공백 추가
        if i > 0:
            result += ' '
        for j in range(len(func[i])):
            if j == 0 and set_coord == i:
                result = result + '[' + func[i][j] + ']'
                is_set = True
                shortcut.add(func[i][j].lower())
            else:
                if is_first:
                    result += func[i][j]
                else:
                    if is_set or func[i][j].lower() in shortcut:
                        result += func[i][j]
                    else:
                        result = result + '[' + func[i][j] + ']'
                        is_set = True
                        shortcut.add(func[i][j].lower())
    # 단축키 설정
    print(result)
