# https://www.acmicpc.net/problem/16916
# 71940KB 656ms
# 다시 풀어보기(참고 : https://bowbowbow.tistory.com/6)

def getTable(P):
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = table[j - 1]
        if P[i] == P[j]:
            j += 1
            table[i] = j

def KMP(S, P):
    getTable(P)
    j = 0
    for i in range(len(S)):
        while j > 0 and S[i] != P[j]:
            j = table[j - 1]
        if S[i] == P[j]:
            if j == len(P) - 1:
                return True
            else:
                j += 1
    return False

S = input()
P = input() # pattern
table = [0] * len(P)

if KMP(S, P):
    print(1)
else:
    print(0)

'''
S = input()
P = input()
if P in S:
    print(1)
else:
    print(0)
'''

'''
S = input()
P = input()
s = len(S)
p = len(P)
flag = False

for i in range(s-p):
    char = ''
    for j in range(i, i+p):
        char += S[j]
        if char == P:
            flag = True
            break
    if flag:
        break
if flag:
    print(1)
else:
    print(0)
'''