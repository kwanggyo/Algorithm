# https://www.acmicpc.net/problem/17413
# 구현
# 32424KB, 116ms

S = list(input())
ans = ''
i = 0
tmp = ''

while i < len(S):
    # 태그로 묶여있는 경우
    if S[i] == '<':
        # 그 전까지 나왔던 문자열을 뒤집어 준 후
        tmp = list(tmp)
        tmp.reverse()
        ans += ''.join(tmp)
        tmp = ''
        # 태그 부분은 그대로
        ans += '<'
        while S[i] != '>':
            i += 1
            ans += S[i]
    # 공백인 경우
    elif S[i] == ' ':
        tmp = list(tmp)
        tmp.reverse()
        ans += ''.join(tmp) + ' '
        tmp = ''
    # 문자인 경우
    else:
        tmp += S[i]
    i += 1

# 태그 없이 끝났을 경우 마지막 문자열 뒤집기
if tmp != '':
    tmp = list(tmp)
    tmp.reverse()
    ans += ''.join(tmp)
    tmp = ''

print(ans)