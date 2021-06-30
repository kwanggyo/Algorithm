T = int(input())
# 우 하 상 좌
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(T):
    N = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    print(sticker)




