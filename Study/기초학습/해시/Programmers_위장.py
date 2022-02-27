# https://programmers.co.kr/learn/courses/30/lessons/42578
# 해시
# 경우의 수 공부,,

def solution(clothes):
    clothes_type = dict()
    # 딕셔너리에 옷 종류를 구분해서 넣어준다.
    for c, type in clothes:
        if type in clothes_type:
            clothes_type[type].append(c)
        else:
            clothes_type[type] = [c]
    # 옷 종류에 해당하는 개수를 파악한다.
    num = []
    for C in clothes_type.values():
        num.append(len(C))
    # 만들 수 있는 조합의 수를 체크
    answer = 1
    for cnt in num:
        # 종류 별로 안입는 경우의 수가 있기 때문에 + 1
        answer *= cnt + 1
    # 다 안입는 경우를 뺴준다.
    answer -= 1

    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))