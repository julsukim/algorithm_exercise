code = ["a=3", "..a=4", "..b=3", "..print a", ".......a=6", ".......print a", ".......print b", "..print a", "....a=7",
        "....print a", "print a", "print b", "a=4", "print a", "...print a"]
result = ["a=4", "a=6", "b=3", "a=4", "a=7", "a=3", "error", "a=4", "a=4"]


def solution(code):
    answer = []

    v_dict = {}
    block_depth = [-1]*1000
    block = 0
    prev_cnt = 0

    def sl_print(codeline):
        if codeline[-1] in v_dict:
            for k in range(block, -1, -1):
                if v_dict[codeline[-1]][k] != '0':
                    answer.append(f'{codeline[-1]}={v_dict[codeline[-1]][k]}')
                    break
            else:
                answer.append('error')
        else:
            answer.append('error')

    def sl_add(codeline):
        if codeline[0] in v_dict:
            v_dict[codeline[0]][block] = codeline[2:]
        else:
            v_dict[codeline[0]] = ['0']*1000
            v_dict[codeline[0]][block] = codeline[2:]

    for i in range(len(code)):
        now = code[i]
        now_cnt = 0

        for c in now:
            if c != '.':
                now = now.lstrip('.')
                break
            now_cnt += 1

        if i==0:
            block_depth[block] = now_cnt
            if len(now.split()) == 2:
                sl_print(now)
            else:
                sl_add(now)
            prev_cnt = now_cnt
            continue

        if now_cnt == prev_cnt:
            if len(now.split()) == 2:
                sl_print(now)
            else:
                sl_add(now)

        elif now_cnt > prev_cnt:
            block += 1
            block_depth[block] = now_cnt

            if len(now.split()) == 2:
                sl_print(now)
            else:
                sl_add(now)

        else:
            delete_list = []
            for b in range(block, -1, -1):
                if now_cnt < block_depth[b]:
                    delete_list.append(b)
                else:
                    block = b
                    break

            for v in v_dict:
                for de in delete_list:
                    v_dict[v][de] = '0'

            if len(now.split()) == 2:
                sl_print(now)

        prev_cnt = now_cnt
    return answer


print(solution(code))

