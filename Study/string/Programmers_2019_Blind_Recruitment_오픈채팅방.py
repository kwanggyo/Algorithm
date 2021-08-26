def solution(record):
    # 1. 첫 알파벳을 보고 나눈다.(E, L C)
    # 2. 딕에 추가해서 바꾸자 ! key : id, value : 닉네임
    answer = []
    tmp = []
    user_dict = dict()
    for val in record:
        split_list = val.split(' ')
        if split_list[0][0] == 'E':
            user_dict[split_list[1]] = split_list[2]
            tmp.append(f'{split_list[1]}:님이 들어왔습니다.')
        elif split_list[0][0] == 'L':
            tmp.append(f'{split_list[1]}:님이 나갔습니다.')
            pass
        else:
            user_dict[split_list[1]] = split_list[2]
    for res in tmp:
        res_li = res.split(':')
        answer.append(f'{user_dict[res_li[0]]}{res_li[1]}')
    return answer