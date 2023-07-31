import sys
sys.stdin  = open('input.txt', 'r')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
visited = [False]*(N+1)
num_list.sort()

def backTracking(result):
    if len(result) == M:
        print(*result)
        return
    for i in range(len(num_list)):
        if visited[i] == False and (len(result)==0 or num_list[i] > result[-1]): 
            visited[i] = True 
            result.append(num_list[i])
            backTracking(result)
            visited[i] = False
            result.pop()
backTracking([])