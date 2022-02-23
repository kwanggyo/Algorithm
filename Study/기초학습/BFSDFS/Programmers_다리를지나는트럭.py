# https://programmers.co.kr/learn/courses/30/lessons/42583
# 스택/큐

# 다시 풀어보기
# 올라간 후 얼마나 이동했는지 확인하는 방법 참고!!
# deque로 popleft()를 쓰면 TC 5번에서 시간초과 -> deque를 없애면 통과
# 다른 사람 코드 참고 - 클래스로 구현한 코드 ↓
# https://programmers.co.kr/learn/courses/30/lessons/42583/solution_groups?language=python3

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 현재 다리 위에 있는지 확인하는 리스트
    on_bridge = [0] * bridge_length

    while len(on_bridge):
        # 시간을 늘려주고 맨 처음에 있는 트럭을 빼준다(자동으로 앞으로 밀리면서 카운트)
        answer += 1
        on_bridge.pop(0)
        # 트럭이 남아 있다면
        if truck_weights:
            # 다리위에 올릴 수 있다면 대기 목록에서 pop해서 올려준다.
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            # 못 올린다면 0을 올려준다.
            else:
                on_bridge.append(0)

    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]	))