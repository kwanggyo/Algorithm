# https://www.acmicpc.net/problem/21314
# Greedy
# 30864KB, 84ms

MG = input()

MG_max = []
MG_min = []
for word in MG.split('K'):
    if word:
        MG_min.append(str(10**(len(word)-1)))
        MG_max.append(str(5*10**(len(word))))
    else :
        MG_min.append('')
        MG_max.append(str(5))

print(''.join(MG_max[:-1])+'1'*(len(MG_max[-1])-1))
print('5'.join(MG_min))