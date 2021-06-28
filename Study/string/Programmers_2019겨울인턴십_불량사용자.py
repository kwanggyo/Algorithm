def comb(N, R):  
    if N < R:
        return N
    else:
        mul = 1
        div = 1
        for i in range(N, N - R, -1):
            mul *= i
        for j in range(1, R + 1):
            div *= j
        return mul // div


def solution(user_id, banned_id):
    answer = 0
    # string + 조합
    # banned_id를 하나씩 꺼내서 글자수를 비교
    # 글자수가 다르면 pass 같으면 비교 시작
    # 밴해야하는 id라면 list에 저장
    # 마지막에 len(list)의 개수에서 len(banned_id)의 개수의 조합을 구함
    # banned_id의 개수가 더 많으면 그냥 len(list)가 답
    ans_set = set()
    ban_dict = {}
    user_dict = {}
    for ban in banned_id:
        B = len(ban)  # banned_id에 글자수에 해당하는 id가 몇개인지 계산
        if B not in ban_dict:
            ban_dict[B] = 1
        else:
            ban_dict[B] += 1
        for user in user_id:
            if len(ban) == len(user):
                flag = True
                for i in range(len(ban)):
                    if ban[i] != '*':
                        if ban[i] == user[i]:
                            continue
                        else:
                            flag = False
                            break
                if flag:
                    ans_set.add(user)

    for ans in ans_set:  # 해당하는 user_id의 글자수를 key로 하는 dict 생성
        N = len(ans)
        if N not in user_dict:
            user_dict[N] = 1
        else:
            user_dict[N] += 1

    answer = 1
    if user_dict: 
        for key in user_dict.keys():
            answer *= comb(user_dict[key], ban_dict[key])
    return answer