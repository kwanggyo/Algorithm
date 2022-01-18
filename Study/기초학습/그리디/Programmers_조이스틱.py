# https://programmers.co.kr/learn/courses/30/lessons/42860
# 그리디
# A : 65, Z : 90

def solution(name):
    answer = 0
    for idx, x in enumerate(name):
        if ord(x) == 65:
            answer += 1
            continue
        # 위로 올리면서 바꾼 횟수가 아래로 내리면서 바꾼 횟수보다 작으면
        elif ord(x) - ord('A') < ord('Z') - ord(x) + 1:
            answer += ord(x) - 65
        # 그렇지 않으면
        else:
            answer += 91 - ord(x)

    return answer

print(solution("JEROEN"))
print(solution("JAN"))



'''
A B C D E F
G H I J K L
M N O P Q R
S T U V W X
Y Z
'''