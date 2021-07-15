# isdigit() -> 숫자인지 확인
# isalpha()
def solution(s):
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    i = 0
    answer = ''
    while i < len(s):
        if ord(s[i]) > 57:
            if s[i] == 'z':
                answer += num_dict['zero']
                i += 4
            elif s[i] == 'o':
                answer += num_dict['one']
                i += 3
            elif s[i] == 't':
                if s[i+1] == 'w':
                    answer += num_dict['two']
                    i += 3
                else:
                    answer += num_dict['three']
                    i += 5
            elif s[i] == 'f':
                if s[i+1] == 'o':
                    answer += num_dict['four']
                    i += 4
                else:
                    answer += num_dict['five']
                    i += 4
            elif s[i] == 's':
                if s[i+1] == 'i':
                    answer += num_dict['six']
                    i += 3
                else:
                    answer += num_dict['seven']
                    i += 5
            elif s[i] == 'e':
                answer += num_dict['eight']
                i += 5
            elif s[i] == 'n':
                answer += num_dict['nine']
                i += 4
        else:
            answer += s[i]
            i += 1
    return int(answer)