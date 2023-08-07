N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

def backTracking(result):
    if len(result) == M:
        print(*result)
        return
    for i in num_list:
        if i in result:
            continue
        result.append(i)
        backTracking(result)
        result.pop()
backTracking([])