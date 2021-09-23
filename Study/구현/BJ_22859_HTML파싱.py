# https://www.acmicpc.net/problem/22859
# 런타임 에러

# div가 몇번 나오는지 체크한다 -> paragraph의 배열을 생성하기 위해
# p가 나오면 paragraph에 차례대로 다 넣는다.
# p에 대해서 안에 있는 태그를 지운다!

import sys
input = sys.stdin.readline
html = input().split('>')
print(html)
cnt = 0
idx = 0
diff_idx = []
title = []
for content in html:
    if content[0] == '<':
        if content[1:4] == 'div':
            cnt += 1
            title.append(content.split('=')[1]) # '"title_name_1"' 이런식으로 들어간다.

paragraph = [list() for _ in range(cnt)]
paragraph_ans = [list() for _ in range(cnt)]
for i in range(len(html)):
    if len(html[i]) >= 2:
        if html[i][1] == '/' and html[i][2:5] == 'div':
            tmp = ''
            for k in range(len(paragraph[idx])):    # paragraph를 나누는 작업
                if paragraph[idx][k][-2] == '/' and paragraph[idx][k][-1] == 'p':
                    tmp += paragraph[idx][k].split('<')[0].strip() + ' '
                    paragraph_ans[idx].append(tmp)
                    tmp = ''
                else:
                    if paragraph[idx][k].split('<')[0].strip() == '':
                        continue
                    else:
                        tmp += paragraph[idx][k].split('<')[0].strip() + ' '
            idx += 1    # div가 끝나면 paragraph의 인덱스를 하나 추가한다.
    if html[i][0] == '<':
        if html[i][1] == 'p':
            start = i + 1
            continue
    if len(html[i]) >= 2:
        if html[i][-2] == '/' and html[i][-1] == 'p':
            end = i + 1
            diff_idx.append(end - start)
            for j in range(start, end):
                paragraph[idx].append(html[j])

for i in range(cnt):
    print('title : ' + title[i][1:len(title[i])-1])
    for j in range(len(paragraph_ans[i])):
        print(paragraph_ans[i][j][:-1])


'''
# 정답 코드
string = input()
divs = string.split('<div title="')
for i in range(1, len(divs)):
    div = divs[i]
    p_list = div.split('<p>')
    title = p_list.pop(0)
    title = title[:-2]
    print('title :', title)
    # p태그들
    for ps in p_list:
        sentence = ''
        j = 0
        while j < len(ps):
            # 태그기호는 다 제거 '<' 나오면 '>' 나올 때까지 스킵
            if ps[j] == '<':
                for k in range(j+1, len(ps)):
                    if ps[k] == '>':
                        j = k
                        break
            else:
                sentence += ps[j]
            j += 1
        # 띄어쓰기 한칸씩만 만들어주기
        result = sentence.split()
        result = ' '.join(result)
        print(result)
'''