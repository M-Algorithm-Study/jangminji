import sys
sys.stdin  = open('input.txt', 'r')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort() # 1 7 9 9
num_list
visited = [False] * (N+1)

def backTracking(result):
    if len(result) == M:
        print(*result)
        return
    for i in range(len(num_list)):
        if visited[i] == False:
            visited[i] = True
            result.append(num_list[i])
            backTracking(result)
            visited[i] = False
            result.pop()
backTracking([])
