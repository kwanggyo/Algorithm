import sys
sys.setrecursionlimit(987654321)
input = sys.stdin.readline  # 이렇게 입력을 받으면 \n이 들어갈 수 있음

N, M = map(int, input().split())
p = [i for i in range(N + 1)]

def findSet(v):
    if v != p[v]:
        p[v] = findSet(p[v])    # p[v]를 안쓰고 return으로 쓰게 되면 구할 때마다 따라간다는 단점이 있지만 바로 위의 노드를 알 수 있다.
    return p[v] # v라고 쓰면 안됨, 재귀를 타고 구한 p[v] 값을 써야함

def union(u, v):
    a = findSet(u)
    b = findSet(v)
    # 랭크를 계산해서 더 깊은 곳에 붙여준다! 지금은 그냥 a < b로 넣어주는데 운 좋게 작은 수(a)가 트리 랭크가 큰거임
    if a < b:
        p[b] = a
    else:
        p[a] = b


for _ in range(M):
    w, u, v = map(int, input().split())
    if w:
        if findSet(u) == findSet(v):
            print('YES')
        else:
            print('NO')
    else:
        union(u, v)