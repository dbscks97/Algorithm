from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque([(priority, idx) for idx, priority in enumerate(priorities)])

    while q:
        cur_priority, cur_idx = q.popleft()
        if any(cur_priority < priority for priority, _ in q):
            q.append((cur_priority, cur_idx))
        else:
            if cur_idx == location:
                return answer
            answer += 1