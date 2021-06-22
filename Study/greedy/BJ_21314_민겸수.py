# 앞에서부터 K가 나올때마다 끊는다.
# 아이디어1
#  : 처음 K가 나올때마다 끊었을 때가 최댓값
#  : K가 들어간 곳을 최대한 쪼갰을 때 최솟값
# 민겸수를 탐색하다가 K가 있으면 거기까지의 값을 리스트에 추가하고 다음 값 비교
# 이 수를 바꾸면 최댓값이 나옴
# 그 후에 리스트의 인덱스에 있는 문자열을 확인해서 K값이 있으면 다시 쪼갠다.
# K값이 있을 때 쪼개는 함수 : 리스트를 인덱스를 받고 새로운 인덱스 반환

def search_max(string):
    div_li = []
    start = 0
    for i in range(len(string)):
        if string[i] == 'K':    # K가 나오면 K를 포함해서 자름
            div_Mingeom_num = ''
            for j in range(start, i + 1):
                div_Mingeom_num += string[j]
            div_li.append(div_Mingeom_num)
            start = i + 1
    if start != len(string):    # 마지막 수를 넣어주는 부분
        div_Mingeom_num = ''
        for k in range(start, len(string)):
            div_Mingeom_num += string[k]
        div_li.append(div_Mingeom_num)
    return div_li


def search_min(li):
    min_li = []
    for char in li:
        start = 0
        for i in range(len(char)):
            if char[i] == 'K':  # K 포함하지 않고 자름
                div_char = ''
                for j in range(start, i):
                    div_char += char[j]
                if len(div_char):   # 마지막 확인
                    min_li.append(div_char)
                start = i
        div_char = ''
        for k in range(start, len(char)):
            div_char += char[k]
        if len(div_char):
            min_li.append(div_char)
    return min_li


def cal(li):
    res = ''
    while li:
        ans = ''
        value = li.pop(0)
        N = len(value)
        if 'K' in value:
            ans = 5 * 10 ** (N - 1)
        else:
            ans = 10 ** (N - 1)
        res += str(ans)
    return int(res)

Mingeom_num = input()
max_li = search_max(Mingeom_num)
min_li = search_min(max_li)
max_res = cal(max_li)
min_res = cal(min_li)
print(max_res)
print(min_res)