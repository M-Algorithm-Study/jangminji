import sys
sys.stdin  = open('input.txt', 'r')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort() # 1 7 9 9
visited = [False]*(N+1)

def backTracking(result):
    prev = 0
    if len(result) == M:      
        print(*result)
        return
    
    for i in range(len(num_list)):
        if len(result) == 0 or visited[i] == False and num_list[i] != prev and num_list[i] >= result[-1]:

            prev = num_list[i]
            visited[i] = True
            result.append(num_list[i])
            backTracking(result)
            visited[i] = False
            result.pop()
backTracking([])

