# 들어가있는 알파벳을 정리하고
# 그 알파벳으로 만들 수 있는 course 자리의 경우의 수(조합)를 만든 후,
# 그 경우의 수가 있는지 확인하고 있으면 cnt + 1,
# cnt >=2 이상이면 멈추고 저장 -> 가지치기


def solution(orders, course):
    alphabet = []
    for order in orders:
        for alpa in order:
            if alpa not in alphabet:
                alphabet.append(alpa)

    def comb(idx, N): 
        if idx == N:
            pass
        else:
            for i in range(len(alphabet)):
                pass

    candidate = []
    for num in course:
        check = [0] * num
        comb(0, num)
    
    
    
    # answer = []
    # return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])