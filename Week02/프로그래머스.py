from collections import deque


def solution(sequence, k):
    answer = []
    sequence += [0]

    q = deque()
    sum = 0
    start, end = 0, 0
    result = len(sequence)
    for i in range(len(sequence)):
        while sum > k:
            temp = q.popleft()
            sum -= temp
            start += 1
        if sum == k and end - start < result:
            answer = [start, end]
            result = end - start

        q.append(sequence[i])
        sum += sequence[i]
        end = i

    return answer