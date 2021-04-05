import sys

sys.stdin = open("input_1231.txt", "r")

# 완전이진트리 - inorder
# 입력을 받아올 때, 0 : 노드번호, 1 : 글자, 2, 3 : 자식노드
# root 부분은 이 문제에서 안해도 됨(주어짐) 참고만!

def dfs(v):
    global ans
    if v == 0: return
    dfs(L[v])
    ans += P[v]
    dfs(R[v])


for tc in range(1, 11):
    V = int(input())
    L = [0] * (V + 1)  # 부모의 왼쪽 자식
    R = [0] * (V + 1)  # 부모의 오른쪽 자식
    P = [0] * (V + 1)  # 부모에 들어가 있는 글자
    pa = [0] * (V + 1)  # 자식에 해당하는 부모를 저장할 거임
    ans = ''

    for i in range(V):
        arr = list(input().split())
        P[int(arr[0])] = arr[1]
        if len(arr) == 3:
            L[int(arr[0])] = int(arr[2])
            # 자식에 해당하는 부모 저장
            pa[int(arr[2])] = int(arr[0])
        elif len(arr) == 4:
            L[int(arr[0])] = int(arr[2])
            R[int(arr[0])] = int(arr[3])
            # 자식에 해당하는 부모 저장
            pa[int(arr[2])] = int(arr[0])
            pa[int(arr[3])] = int(arr[0])

    # root 찾기
    root = 0
    for i in range(1, V + 1):
        if pa[i] == 0:
            root = i
            break

    dfs(root)
    print('#{} {}'.format(tc, ans))